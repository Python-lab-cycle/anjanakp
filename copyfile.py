file1=input("Enter first filename:")
file2=input("Enter second file name:")
fn1 = open(file1,'r')
fn2 = open(file2,'w')
cont = fn1.read();
fn2.write(cont);
fn1.close();
fn2.close();
