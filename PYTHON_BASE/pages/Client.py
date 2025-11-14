
from sqlalchemy.orm import *
from CHECK_0 import Client,create_engine
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
st.title('Client')
Surname = st.text_area('Client surname')
Name = st.text_area('Client name')
Patronymic = st.text_area('Client patronymic')
Phone = st.number_input('Client phone',
                        max_value = 100000000000,
                        min_value = 1,
                        value = 1)
submit = st.button('Complite')
if submit and Surname and Name and Patronymic and Phone:
    try:
        entry = Client(surname=Surname,name=Name,
                       patronymic=Patronymic,phone=Phone)
        sess.add(entry)
        sess.commit()
        st.success('done')
    except Exception as e:
        st.error(f'Some problem with:{e}')
if st.checkbox('view data'):
    result = sess.query(Client).all()
    for item in result:
        st.text(item.surname)
        st.text(item.name)
        st.text(item.patronymic)
        st.text(item.phone)
