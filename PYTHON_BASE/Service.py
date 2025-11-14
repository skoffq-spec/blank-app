
from sqlalchemy.orm import *
from CHECK_0 import service,create_engine
import streamlit as st
import logging
from st_pages import *
import pandas as pd
from numpy.random import default_rng as rng
for name, l in logging.root.manager.loggerDict.items():
    if "streamlit" in name:
        l.disabled = True
engine = create_engine('sqlite:///project_db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session() 


st.title('SERVICE')
Service = st.text_area('Name of service')
Price = st.number_input('Price of service',
                        max_value = 100000,
                        min_value = 1,
                        value = 1)
submit = st.button('Complite')
if submit and Service:
    try:
        entry = service(name=Service,price=Price)
        sess.add(entry)
        sess.commit()
        st.success('done')
    except Exception as e:
        st.error(f'Some problem with:{e}')
if st.checkbox('view data'):
    result = sess.query(service).all()
    for item in result:
        st.text(item.name)
        st.text(item.price)
st.set_page_config(
    page_title="SCHEDULE_BASE",
    page_icon="💾",
)
editable_database = pd.DataFrame('r')
database_ed = st.data_editor(editable_database,num_rows='dynamic')
if st.buton('Save Changes'):
    st.write('Updated DataFrame:')
    st.write(database_ed)
         
