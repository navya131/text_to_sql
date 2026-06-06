import re

def generate_sql(prompt):

    prompt_lower = prompt.lower()

    # -------------------------
    # TABLE DETECTION
    # -------------------------
    tables = [
        "employees",
        "students",
        "users",
        "products",
        "customers",
        "orders",
        "teachers",
        "books"
    ]

    table_name = "table_name"

    for table in tables:
        if table in prompt_lower:
            table_name = table
            break

    # -------------------------
    # COLUMN DETECTION
    # -------------------------
    possible_columns = [
        "id",
        "name",
        "salary",
        "department",
        "age",
        "price",
        "rating",
        "email",
        "phone",
        "quantity",
        "marks",
        "city"
    ]

    columns = []

    for col in possible_columns:
        if re.search(r'\b' + col + r'\b', prompt_lower):
            columns.append(col)

    selected_columns = "*"

    if columns:
        selected_columns = ", ".join(columns)

    # -------------------------
    # CONDITIONS
    # -------------------------
    conditions = []

    numeric_fields = [
        "salary",
        "age",
        "marks",
        "price",
        "quantity",
        "rating",
        "id"
    ]

    for field in numeric_fields:

        gt = re.search(
            rf"{field}.*(?:>|greater than|above|more than)\s*(\d+)",
            prompt_lower
        )

        if gt:
            conditions.append(
                f"{field} > {gt.group(1)}"
            )

        lt = re.search(
            rf"{field}.*(?:<|less than|below|under)\s*(\d+)",
            prompt_lower
        )

        if lt:
            conditions.append(
                f"{field} < {lt.group(1)}"
            )

        eq = re.search(
            rf"{field}.*(?:=|is)\s*(\d+)",
            prompt_lower
        )

        if eq:
            conditions.append(
                f"{field} = {eq.group(1)}"
            )

    # -------------------------
    # DEPARTMENT
    # -------------------------
    dept = re.search(
        r"department\s+(?:is|=)\s+([a-zA-Z]+)",
        prompt,
        re.IGNORECASE
    )

    if dept:
        conditions.append(
            f"department = '{dept.group(1)}'"
        )

    # -------------------------
    # CITY
    # -------------------------
    city = re.search(
        r"city\s+(?:is|=)\s+([a-zA-Z]+)",
        prompt,
        re.IGNORECASE
    )

    if city:
        conditions.append(
            f"city = '{city.group(1)}'"
        )

    # -------------------------
    # NAME
    # -------------------------
    name = re.search(
        r"name\s+(?:is|=)\s+([a-zA-Z]+)",
        prompt,
        re.IGNORECASE
    )

    if name:
        conditions.append(
            f"name = '{name.group(1)}'"
        )

    # -------------------------
    # LIMIT
    # -------------------------
    limit = ""

    top = re.search(r"top\s+(\d+)", prompt_lower)

    if top:
        limit = f" LIMIT {top.group(1)}"

    elif "generate" in prompt_lower:

        num = re.search(r"(\d+)", prompt_lower)

        if num:
            limit = f" LIMIT {num.group(1)}"

    # -------------------------
    # DELETE
    # -------------------------
    if "delete" in prompt_lower or "remove" in prompt_lower:

        query = f"DELETE FROM {table_name}"

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        return query + ";"

    # -------------------------
    # UPDATE
    # -------------------------
    if "update" in prompt_lower:

        query = f"UPDATE {table_name} SET column_name='new_value'"

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        return query + ";"

    # -------------------------
    # INSERT
    # -------------------------
    if "insert" in prompt_lower or "add" in prompt_lower:

        return (
            f"INSERT INTO {table_name} "
            "(column1,column2) "
            "VALUES('value1','value2');"
        )

    # -------------------------
    # COUNT
    # -------------------------
    if "count" in prompt_lower:

        query = f"SELECT COUNT(*) FROM {table_name}"

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        return query + ";"

    # -------------------------
    # AVG
    # -------------------------
    if "average" in prompt_lower:

        if "salary" in prompt_lower:
            return f"SELECT AVG(salary) FROM {table_name};"

        if "marks" in prompt_lower:
            return f"SELECT AVG(marks) FROM {table_name};"

    # -------------------------
    # MAX
    # -------------------------
    if "maximum" in prompt_lower or "highest" in prompt_lower:

        if "salary" in prompt_lower:
            return f"SELECT MAX(salary) FROM {table_name};"

        if "marks" in prompt_lower:
            return f"SELECT MAX(marks) FROM {table_name};"

    # -------------------------
    # SELECT
    # -------------------------
    query = f"SELECT {selected_columns} FROM {table_name}"

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    query += limit

    return query + ";"