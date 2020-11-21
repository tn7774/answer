NC = 256
def m_char(s, n): 
    count = [0] * NC 
    for i in range(n): 
        count[ord(s[i])] += 1
    mt = 0
    for i in range(NC): 
        if (count[i] != 0): 
            mt += 1    
    return mt 
def find_str(s): 
    n = len(s)     
    mt = m_char(s, n) 
    mi = n      
    for i in range(n): 
        for j in range(n): 
            z = s[i:j] 
            z_l = len(z) 
            s_char = m_char(z, z_l) 
            if (z_l < mi and 
                mt == s_char): 
                mi = z_l 
    return mi  
s = input()
l = find_str(s); 
print(l)
