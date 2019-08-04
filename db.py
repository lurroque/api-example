import pymysql

conn = pymysql.connect(
    user="root",
    password="api",
    db="api",
    cursorclass=pymysql.cursors.DictCursor,
)


def create_property(property_):
    cur = conn.cursor()
    cur.execute(
        """insert into imovel(
                        name,
                        address,
                        description,
                        status,
                        features,
                        type_of,
                        purpose,
                        real_estate)
                        values(%s, %s, %s, %s, %s, %s, %s, %s)""",
        (
            property_["name"],
            property_["address"],
            property_["description"],
            property_["status"],
            property_["features"],
            property_["type_of"],
            property_["purpose"],
            property_["real_estate"],
        ),
    )
    conn.commit()
    id_ = cur.lastrowid
    cur.close()
    return id_


def list_properties():
    cur = conn.cursor()
    cur.execute("select * from imovel;")
    properties = cur.fetchall()
    cur.close()
    return properties


def delete_property(id_):
    cur = conn.cursor()
    cur.execute("delete from imovel where id=%s;", (id_,))
    conn.commit()
    cur.close()


def exist_property(id_):
    cur = conn.cursor()
    cur.execute("select count(*) from imovel where id=%s;", (id_,))
    exists = cur.fetchone()["count(*)"] != 0
    cur.close()
    return exists


def update_property(property_, identifier):
    cur = conn.cursor()
    cur.execute(
        """update imovel set
                        name=%s,
                        address=%s,
                        description=%s,
                        status=%s,
                        features=%s,
                        type_of=%s,
                        purpose=%s,
                        real_estate=%s where id=%s""",
        (
            property_["name"],
            property_["address"],
            property_["description"],
            property_["status"],
            property_["features"],
            property_["type_of"],
            property_["purpose"],
            property_["real_estate"],
            identifier,
        ),
    )
    conn.commit()
    cur.close()


def create_real_estate(real_estate):
    cur = conn.cursor()
    cur.execute(
        """insert into real_estate(
                        name,
                        address,
                        values(%s, %s)""",
        (
            real_estate["name"],
            real_estate["address"],
        ),
    )
    conn.commit()
    id_ = cur.lastrowid
    cur.close()
    return id_


def list_real_estates():
    cur = conn.cursor()
    cur.execute("select * from real_estate;")
    real_estates = cur.fetchall()
    cur.close()
    return real_estates


def delete_real_estate(id_):
    cur = conn.cursor()
    cur.execute("delete from real_estate where id=%s;", (id_,))
    conn.commit()
    cur.close()


def exist_real_estate(id_):
    cur = conn.cursor()
    cur.execute("select count(*) from real_estate where id=%s;", (id_,))
    exists = cur.fetchone()["count(*)"] != 0
    cur.close()
    return exists


def update_real_estate(real_estate, identifier):
    cur = conn.cursor()
    cur.execute(
        """update real_estate set
                        name=%s,
                        address=%s where id=%s""",
        (
            real_estate["name"],
            real_estate["address"],
        ),
    )
    conn.commit()
    cur.close()
