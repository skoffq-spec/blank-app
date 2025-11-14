
from sqlalchemy.orm import *
from CHECK_0 import *
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
st.title('Gift')
Dascription = st.text_area('Gift dascription')
submit = st.button('Complite')
if submit and Dascription:
    try:
        entry = Gift(dascription=Dascription)   
        sess.add(entry)
        sess.commit()
        st.success('done')
    except Exception as e:
        st.error(f'Some problem with:{e}')
if st.checkbox('view data'):
    result = sess.query(Gift).all()
    for item in result:
        st.text(item.dascription)