## Definisi Kelas ##
## Definisi Kelas MyListElement
## Nama: Khresna Mulia Putra (Khresmupu)
## NRP: 2572032

## Definisi Atribut:
# info  : atribut yang menyimpan nilai (integer)
# next  : atribut reference elemen berikutnya
#         (Node)
class MyListElement:
    def __init__(self,value):
        self.info=value
        self.next=None

## Definisi Atribut:
# head  : atribut yang menyimpan nilai awal
#        (MyListElement)
# tail  : atribut yang menyimpan nilai akhir
#        (MyListElement)
class QueueList:
    def __init__(self):
        self.head=None
        self.tail=None
    def traversal(self):
        if self.head==None:
            print("List kosong")
        else:
            p=self.head
            while p!=None:
                print(f"{p.info} ",end="")
                p=p.next
            print()
    def enqueue(self,x):
        if self.head==None:
            self.head=x
            self.tail=x
        else:
            self.tail.next=x
            self.tail=x
    def dequeue(self):
        if self.head==None:
            print("Antrian Kosong")
        else:
            if self.head==self.tail:
                self.head=None
                self.tail=None
            else:
                self.head = self.head.next
    # count : menyimpan jumlah(int)
    def size(self):
        p=self.head
        count=0
        while p != None:
            count = count + 1
            p = p.next
        return count
    # count : alat ukur(int)
    def viewElement(self,x):
        if self.head==None:
            print("Antrian Kosong")
        else:
            if x<1 or x>self.size():
                print("Indeks melebihi jumlah elemen antrian!")
            else:
                p = self.head
                count = 1
                while count < x:
                    p = p.next
                    count += 1
                print(f"Elemen antrian ke-{x} : {p.info}")

# Kamus Data (Main Program):
# p             : Gambaran objek list angka 
#                   (MyListElement)
# tanyaObjek    : sebagai input(integer)
# pilih         : pilih menu (integer)
def main():
    p=QueueList()
    print("-------------")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Size")
    print("4. View Element")
    print("0. Exit")
    while True:
        pilih=int(input("Pilih menu: "))
        if pilih<0 or pilih>4:
            print("pilihan tidak valid")
        else:
            if pilih==0:
                p.traversal()
                print("Program selesai!")
                break
            if pilih==1:
                tanyaObjek=MyListElement(int(input("Bilangan: ")))
                p.enqueue(tanyaObjek)
            if pilih==2:
                p.dequeue()
            if pilih==3:
                x=p.size()
                print("Jumlah antrian: ",x)
            if pilih==4:
                tanyaObjek=int(input("Antrian ke berapa? "))
                p.viewElement(tanyaObjek)           
            p.traversal()
            
if __name__ == '__main__':
    main()