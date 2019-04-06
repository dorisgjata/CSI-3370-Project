
DROP FUNCTION IF EXISTS "addUser"(userIdToken VARCHAR, userName TEXT, userLastName TEXT ,userEmail TEXT, isAdmin BOOLEAN);
CREATE OR REPLACE FUNCTION "addUser"(userIdToken VARCHAR, userName TEXT, userLastName TEXT ,userEmail TEXT, isAdmin BOOLEAN)

        RETURNS TEXT
AS $BODY$
DECLARE
        _email TEXT;
BEGIN
        IF EXISTS (
                SELECT
                        $4
                FROM
                        Users
                WHERE
                        users.userEmail = $4) THEN
                RETURN -1;
        ELSE
                INSERT INTO users(userIdToken, userName , userLastName ,userEmail, isAdmin)

                VALUES ($1, $2, $3, $4, $5)
        RETURNING userEmail INTO _email;
                RETURN _email;
        END IF;
END;
$BODY$
LANGUAGE plpgsql VOLATILE NOT LEAKPROOF;
