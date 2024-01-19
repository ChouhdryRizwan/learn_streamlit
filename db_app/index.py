# streamlit_app.py

import streamlit as st

# Create the SQL connection to db_org  as specified in your secrets file.
conn = st.connection('db_org', type='sql')

# Insert some data with conn.session.
with conn.session as s:
    s.execute('CREATE TABLE IF NOT EXISTS tbl_emp (emp_id NUMBER, emp_name TEXT);')
    s.execute('DELETE FROM tbl_emp;')
    tbl_emp = {'1': 'Rizwan', '2': 'Alam', '3': 'Usama'}
    for k in tbl_emp:
        s.execute(
            'INSERT INTO tbl_emp (emp_id, emp_name) VALUES (:emp_id, :emp_name);',
            params=dict(emp_id=k, emp_name=tbl_emp[k])
        )
    s.commit()

# Query and display the data you inserted
tbl_emp = conn.query('select * from tbl_emp')
st.dataframe(tbl_emp)

