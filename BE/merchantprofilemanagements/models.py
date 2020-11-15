from utils import mysql_connection_pool, response_json
from main import jwt_custom_authen


# author: nmcuong
# description: get data for table merchant profile language
# parameter: NONE
# output: object
def get_table_merchant_profile():
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection_pool.get_connection_pool()
        cursor = connection.cursor()
        sql_profile = """SELECT * FROM profile_info WHERE is_deleted = 0"""
        cursor.execute(sql_profile)
        table_data = cursor.fetchall()
        response['code'] = 0
        response['table_data'] = table_data

    except Exception as e:
        print('merchantprofilemanagements.models -> get_table_merchant_profile -> ex: ', e)

    finally:
        mysql_connection_pool.release_connection_pool(cursor, connection)

    return response


# author: nmcuong
# description: search data table merchant profile
# parameter: merchant_name, abbreviation, language, status
# output: object
def search_table_merchant_profile(merchant_name, abbreviation, language, status):
    str_where = ""
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection_pool.get_connection_pool()
        cursor = connection.cursor()
        if merchant_name != '':
            if str_where != '':
                str_where += ' AND '
            str_where += f"pi.profile_name LIKE LCASE('%{merchant_name}%')"

        if abbreviation != '':
            if str_where != '':
                str_where += ' AND '
            str_where += f"pi.abbreviation LIKE LCASE('%{abbreviation}%')"

        if language != '':
            if str_where != '':
                str_where += ' AND '
            str_where += f"pi.default_language = {language}"

        if status != '':
            if str_where != '':
                str_where += ' AND '
            str_where += f"pi.status = {status}"

        sql_profile = 'SELECT * FROM profile_info pi'

        if str_where != '':
            sql_profile += f" WHERE {str_where}"
        cursor.execute(sql_profile)
        table_data = cursor.fetchall()
        response['code'] = 0
        response['table_data'] = table_data

    except Exception as e:
        print('merchantprofilemanagements.models -> search_table_merchant_profile -> ex: ', e)

    finally:
        mysql_connection_pool.release_connection_pool(cursor, connection)

    return response


# author: nmcuong
# description: get data for combo box language
# parameter: NONE
# output: object
def get_combobox_language():
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection_pool.get_connection_pool()
        cursor = connection.cursor()
        sql_profile = """SELECT id, name FROM mt_language WHERE is_deleted = 0"""
        cursor.execute(sql_profile)
        table_data = cursor.fetchall()
        response['code'] = 0
        response['table_data'] = table_data

    except Exception as e:
        print('merchantprofilemanagements.models -> get_combobox_language -> ex: ', e)

    finally:
        mysql_connection_pool.release_connection_pool(cursor, connection)

    return response


# author: nmcuong
# description: delete data table merchant profile
# parameter: NONE
# output: object
def delete_merchant_profile(profile_info_id):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection_pool.get_connection_pool()
        cursor = connection.cursor()

        # get id of table profile when id = profile_id in table profile_info
        sql_profile_id = """SELECT profile_id FROM profile_info WHERE id = %s AND is_deleted = 0"""
        cursor.execute(sql_profile_id, profile_info_id)
        profile_info_data = cursor.fetchone()
        profile_id = profile_info_data["profile_id"]

        # delete row in table profile_info
        sql_delete_profile_info = """DELETE FROM profile_info WHERE id = %s"""
        cursor.execute(sql_delete_profile_info, profile_info_id)

        # delete row in table contact
        sql_delete_contact = """DELETE FROM contact WHERE profile_id = %s"""
        cursor.execute(sql_delete_contact, profile_id)

        # delete row in table features
        sql_delete_features = """DELETE FROM features WHERE profile_id = %s"""
        cursor.execute(sql_delete_features, profile_id)

        # delete row in table fee
        sql_delete_fee = """DELETE FROM fee WHERE profile_id = %s"""
        cursor.execute(sql_delete_fee, profile_id)
        connection.commit()
        response['code'] = 0

    except Exception as e:
        print('merchantprofilemanagements.models -> get_combobox_language -> ex: ', e)

    finally:
        mysql_connection_pool.release_connection_pool(cursor, connection)

    return response


# author: nmcuong
# description: init form create profile information
# parameter: NONE
# output: object
def init_create_profile_information():
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection_pool.get_connection_pool()
        cursor = connection.cursor()
        sql_get_language = """SELECT id, name FROM mt_language WHERE is_deleted = 0"""
        cursor.execute(sql_get_language)
        language_data = cursor.fetchall()
        response['language_data'] = language_data

        sql_get_country = """SELECT id, name FROM mt_country WHERE is_deleted = 0"""
        cursor.execute(sql_get_country)
        country_data = cursor.fetchall()
        response['country_data'] = country_data

        sql_get_currency = """SELECT id, name FROM mt_currency WHERE is_deleted = 0"""
        cursor.execute(sql_get_currency)
        currency_data = cursor.fetchall()
        response['currency_data'] = currency_data
        response['code'] = 0

    except Exception as e:
        print('merchantprofilemanagements.models -> init_create_profile_information -> ex: ', e)

    finally:
        mysql_connection_pool.release_connection_pool(cursor, connection)

    return response


# author: nmcuong
# description: create profile information
# parameter: NONE
# output: object
def create_profile_information(request, obj_input):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)

    USER_REQUEST_INFO = jwt_custom_authen.get_user_info_request(request)

    try:
        connection = mysql_connection_pool.get_connection_pool()
        cursor = connection.cursor()

        GLB_USER_INFO = USER_REQUEST_INFO["GLB_USER_INFO"]

        # insert data table profile
        sql_profile = """INSERT INTO profile (user_id, created_time, created_by) VALUES (%s, NOW(), %s)"""
        cursor.execute(sql_profile, (USER_REQUEST_INFO["GLB_USER_ID"], GLB_USER_INFO["full_name"]))

        # get primarry key (profile_id) of inserted row
        profile_id = cursor.lastrowid

        # insert data table profile_info
        sql_profile_info = """INSERT INTO profile_info (profile_id, base_country, base_currency, default_language, profile_name, abbreviation, status, website_url, tax_id, tid, dba_name, mcc, created_time, created_by)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), %s)"""
        cursor.execute(sql_profile_info, (profile_id, obj_input["base_country"], obj_input["base_currency"], obj_input["default_language"], obj_input["profile_name"], obj_input["abbreviation"], obj_input["status"], obj_input["website_url"], obj_input["tax_id"], obj_input["tid"], obj_input["dba_name"], obj_input["mcc"], GLB_USER_INFO["full_name"]))

        # insert data table contacts
        sql_contacts = """INSERT INTO contact (profile_id, street_name, city, state, send_initial_email, phone_number, created_time, created_by)
                VALUES (%s, %s, %s, %s, %s, %s, NOW(), %s)"""
        cursor.execute(sql_contacts, (profile_id, obj_input["street_name"], obj_input["city"], obj_input["state"], obj_input["send_initial_email"], obj_input["phone_number"], GLB_USER_INFO["full_name"]))

        # insert data table features
        sql_features = """INSERT INTO features (profile_id, email_pay, qr_code, subscription, refund, default_email_receipt, default_payment_mode, created_time, created_by)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, NOW(), %s)"""
        cursor.execute(sql_features, (profile_id, obj_input["email_pay"], obj_input["qr_code"], obj_input["subscription"], obj_input["refund"], obj_input["default_email_receipt"], obj_input["default_payment_mode"], GLB_USER_INFO["full_name"]))

        # insert data table fees
        sql_fee = """INSERT INTO fee (profile_id, payment_mechanism, setup_charge, annual_charge, per_transaction_fee, per_transaction_rate, per_successful_rate, refund_return_rate, comments, created_time, created_by)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), %s)"""
        cursor.execute(sql_fee, (profile_id, obj_input["payment_mechanism"], obj_input["setup_charge"], obj_input["annual_charge"], obj_input["per_transaction_fee"], obj_input["per_transaction_rate"], obj_input["per_successful_rate"], obj_input["refund_return_rate"], obj_input["comments"], GLB_USER_INFO["full_name"]))

        connection.commit()
        response['code'] = 0

    except Exception as e:
        print('merchantprofilemanagements.models -> create_profile_information -> ex: ', e)
        connection.rollback()
    finally:
        mysql_connection_pool.release_connection_pool(cursor, connection)

    return response


# author: nmcuong
# description: init screen profile information detail
# parameter: NONE
# output: object
def init_profile_information_detail(profile_info_id):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection_pool.get_connection_pool()
        cursor = connection.cursor()

        #get id of table profile when id = profile_id in table profile_info
        sql_profile_id = """SELECT profile_id FROM profile_info WHERE id = %s AND is_deleted = 0"""
        cursor.execute(sql_profile_id, profile_info_id)
        profile_info_data = cursor.fetchone()
        profile_id = profile_info_data["profile_id"]

        #get data in table profile_info
        sql_get_profile_info = """SELECT profile_id, base_country, base_currency, default_language, profile_name, abbreviation, status, website_url, tax_id, tid, dba_name, mcc FROM profile_info WHERE id = %s AND is_deleted = 0"""
        cursor.execute(sql_get_profile_info, profile_info_id)
        profile_info_data = cursor.fetchone()
        response['profile_info_data'] = profile_info_data

        # get data in table contact
        sql_get_contact = """SELECT street_name, city, state, send_initial_email, phone_number FROM contact WHERE profile_id = %s AND is_deleted = 0"""
        cursor.execute(sql_get_contact, profile_id)
        contact_data = cursor.fetchone()
        response['contact_data'] = contact_data

        # get data in table features
        sql_get_features = """SELECT email_pay, qr_code, subscription, refund, default_email_receipt, default_payment_mode FROM features WHERE profile_id = %s AND is_deleted = 0"""
        cursor.execute(sql_get_features, profile_id)
        features_data = cursor.fetchone()
        response['features_data'] = features_data

        # get data in table fee
        sql_get_fee = """SELECT payment_mechanism, setup_charge, annual_charge, per_transaction_fee, per_transaction_rate, per_successful_rate, refund_return_rate, comments FROM fee WHERE profile_id = %s AND is_deleted = 0"""
        cursor.execute(sql_get_fee, profile_id)
        fee_data = cursor.fetchone()
        response['fee_data'] = fee_data
        response['code'] = 0

    except Exception as e:
        print('merchantprofilemanagements.models -> init_profile_information_detail -> ex: ', e)

    finally:
        mysql_connection_pool.release_connection_pool(cursor, connection)

    return response