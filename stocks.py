import pandas as pd
import sys

def main(fr=sys.stdin,out=sys.stdout):
    m,k,d = map(int,fr.readline().split())
    st=[]
    for _ in range(k):
        st.append(fr.readline().split())
    print(m,k,d,st)

if __name__ == '__main__':
    main()