def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rows = []
    
    for i in range(size-1,-1,-1):
        left= alphabet[size-1:i:-1]
        right= alphabet[i:size]
        
        s= '-'.join(left+right)
        row = s.center(4*size -3,'-')
        rows.append(row)
        
    print('\n'.join(rows+rows[-2::-1]))

         
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
