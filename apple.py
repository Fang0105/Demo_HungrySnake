import setting as st
import random



def getRandomAppleLocation():
    st.imageAppleLocation = (st.transformCoordinateTolocation(random.randint(0, 15),random.randint(0, 15)))
    return st.imageAppleLocation