import pymysql
import datetime
from conf import config


class DB_Connect:
    """
    Класс реализующий функции для управления Базой Данных.
    """
    def __init__(self):
        try:
            self.connection = pymysql.connect(host=config.HOST, port=config.PORT, user=config.USERNAME,
                                              password=config.PASSWORD, database=config.DATABASE_NAME,
                                              cursorclass=pymysql.cursors.DictCursor)
        except RuntimeError as RnE:
            raise RuntimeError("Ошибка соединения с Базой данных. Проверьте запущен ли сервер и повторите попытку!")

    def information_out(self, table_name):
        """
        Функиця для извлечения информации из БД.
        :param table_name: Название таблицы для вывода информации из нее.
        :return: Информация из таблицы.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {table_name}")
                info = cursor.fetchall()
        except pymysql.err.OperationalError as e:
            print("Operation Error  -  " + repr(e))
            info = "Operation Error"
            self.connection.close()
        return info

    def param_information_out(self, table_name, param_name, param):
        """
        Поиск значений по определенным параметрам.
        :param table_name: Название таблицы для поиска.
        :param param_name: Название параметра для поиска.
        :param param: Значение параметра для поиска.
        :return: Найденная информация из БД
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {table_name} WHERE {param_name}={param}")
                info = cursor.fetchall()
        except pymysql.err.OperationalError as e:
            print("Operation Error  -  " + repr(e))
            info = "Operation Error"
            self.connection.close()
        return info

    def save_new_client(self, info):
        """
        Функция для сохранения нового Юридического лица.
        :param info: Информация о новом Юридическом лице.
        :return: Статус сохранения
        """
        try:
            date_str = info[3][6:11] + '-' + info[3][3:5] + '-' + info[3][:2]
            date_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO `legal_entities` (`first_name`, `second_name`, `father_name`, `date_of_birth`) "
                               "VALUES (%s, %s, %s, %s)", (info[0], info[1], info[2], date_date))
                self.connection.commit()

                cursor.execute("SELECT * FROM `legal_entities`")
                manager_id = cursor.fetchall()[-1]["manager_id"]

                cursor.execute(
                    "INSERT INTO `appropriation` (`manager_id`, `activity_id`, `registration_date`, `city_id`, "
                    "`close_doc_id`) VALUES (%s, %s, %s, %s, %s)",
                    (manager_id, info[4], datetime.date.today(), info[5], 0))
                info = "informaton_saved"
                self.connection.commit()
        except pymysql.err.OperationalError as e:
            print("Operation Error  -  " + repr(e))
            info = "Operation Error"
            self.connection.close()
        return info

    def save_new_activity(self, info):
        """
        Функция для сохранения нового вида деятельности уже существующему Юридическому лицу.
        :param info: Информация о новом виде деятельности.
        :return: Статус сохранения.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT `manager_id` FROM `legal_entities` WHERE `first_name`=%s AND `second_name`=%s"
                               " AND `father_name`=%s", (info[0], info[1], info[2]))
                manager_id = cursor.fetchone()['manager_id']

                cursor.execute(f"SELECT `activity_id` FROM `appropriation` WHERE `manager_id`={manager_id}")
                activities = cursor.fetchall()
                client_activities = []
                for activity in activities:
                    client_activities.append(activity['activity_id'])
                print(client_activities)

                if info[4] not in client_activities:
                    cursor.execute(
                        "INSERT INTO `appropriation` (`manager_id`, `activity_id`, `registration_date`, `city_id`, "
                        "`close_doc_id`) VALUES (%s, %s, %s, %s, %s)",
                        (manager_id, info[4], datetime.date.today(), info[5], 0))
                info = "informaton_saved"
                self.connection.commit()
        except pymysql.err.OperationalError as e:
            print("Operation Error  -  " + repr(e))
            info = "Operation Error"
            self.connection.close()
        return info

    def client_is_in_db(self, info: list):
        """
        Проверка наличия Юридического лица в БД.
        :param info: Информация для поиска.
        :return: Статус наличия Юридического лица в БД.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT `manager_id` FROM `legal_entities` WHERE `first_name`=%s AND `second_name`=%s"
                               " AND `father_name`=%s", (info[0], info[1], info[2]))
                if cursor.fetchone() is not None:
                    return True
                else:
                    return False

        except pymysql.err.OperationalError as e:
            print("Operation Error  -  " + repr(e))
            self.connection.close()

    def search_client(self, info):
        """
        Функция для поиска определенного Юридического лица.
        :param info: Параметры Юридического лица для поиска.
        :return: Найденная информация из БД.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT `manager_id` FROM `legal_entities` WHERE `first_name`=%s AND `second_name`=%s"
                               " AND `father_name`=%s", (info[0], info[1], info[2]))
                manager_id = cursor.fetchone()
                print(manager_id)

                client_activities_list = []
                if manager_id is not None:
                    manager_id = manager_id["manager_id"]

                    cursor.execute(f"SELECT * FROM `appropriation` WHERE `manager_id`={manager_id} AND `close_doc_id`={0}")
                    client_activities_hash = cursor.fetchall()
                    print("appropriations = ", client_activities_hash)
                    appropriations = []
                    for activity_hash in client_activities_hash:
                        appropriations.append(list(activity_hash.values()))
                        print("appropriations2 = ", appropriations)

                    for activity in appropriations:
                        cursor.execute(f"SELECT * FROM `activities` WHERE `activity_id`={activity[2]}")
                        activity_info = cursor.fetchone()
                        cache = [i for i in list(activity_info.values())]
                        cursor.execute(f"SELECT `city_name` FROM `discount_cities` WHERE `city_id`={activity[4]}")
                        city_name = cursor.fetchone()["city_name"]
                        cache.append(city_name)
                        cache.append(activity[1])
                        cache.append(activity[0])
                        client_activities_list.append(cache)

                    print(client_activities_list)

        except pymysql.err.OperationalError as e:
            print("Operation Error  -  " + repr(e))
            self.connection.close()
        return client_activities_list

    def remove_activity(self, info):  # Удаление вида деятельности
        """
        Функция для удаления вида деятельности у Юридического лица.
        :param info: Параметры для поиска Юридического лица и вида деятельности.
        :return:
        """
        print(info)
        try:
            with self.connection.cursor() as cursor:
                print("INN - " + str(info[6]))
                cursor.execute("INSERT INTO `close_documents` (`inn`, `date_of_closing`, `close_reason_id`) "
                               "VALUES (%s, %s, %s)", (int(info[6]), datetime.date.today(), int(info[7])))
                self.connection.commit()

                cursor.execute("SELECT `doc_id` FROM `close_documents` WHERE `inn`=%s", (int(info[6])))
                doc_id = cursor.fetchone()['doc_id']
                print(doc_id)

                cursor.execute("UPDATE `appropriation` SET `close_doc_id`=%s WHERE `inn`=%s",
                               (int(doc_id), int(info[6])))
                self.connection.commit()

        except pymysql.err.OperationalError as e:
            print("Operation Error  -  " + repr(e))
            self.connection.close()

    def check_user_existing(self, info):
        """
        Проверка наличия Юридического лица в БД.
        :param info: Информация для поиска.
        :return: Статус наличия Юридического лица в БД.
        """
        existing = False
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM `legal_entities`")
                clients_hash = cursor.fetchall()
                for client in clients_hash:
                    if list(client.values())[1] == info[0] and list(client.values())[2] == info[1] and list(client.values())[3] == info[2]:
                        existing = True

        except pymysql.err.OperationalError as e:
            print("Operation Error  -  " + repr(e))
            self.connection.close()
        return existing

    def close_conn(self):
        """
        Закрытие соединения с БД
        :return:
        """
        self.connection.close()

