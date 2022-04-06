import setting as st
import random

def getRandomAppleLocation():
    st.imageAppleLocation = (222.5 + st.latticeSize * random.randint(0, 15), 0 + st.latticeSize * random.randint(0, 15))
    return st.imageAppleLocation