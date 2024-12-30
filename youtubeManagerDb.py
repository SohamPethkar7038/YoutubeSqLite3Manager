import sqlite3

conn=sqlite3.connect('youtubeManagerDb')

cursor=conn.cursor()

cursor.execute('''               
               create table if not exists videos(
                   Id integer primary key,
                   Name text not null,
                   time text not null
               )
''')

    

def listAllVideos():
    print("\n")
    print("*"* 70)
    print("\n")
    cursor.execute("select * from videos")
    for row in cursor.fetchall():
        print(row)
    print("\n")
    print("*"*70) 
    print("\n")   



def addVideo(Name,Time):
    cursor.execute("insert into videos(Name,Time)values(?,?) ",(Name,Time))
    conn.commit()
    

def updateVideo(videoId,newName,newTime):
    cursor.execute("update videos set Name=? ,Time=? where Id =?",(newName,newTime,videoId))
    conn.commit();


def deleteVideo(video_Id):
    cursor.execute("delete from videos where ID=?",(video_Id,))
    conn.commit()

def main():
    while True:
        
        print("\n Youtube Manager app with DB")
        print("1.List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit Videos")
        
        choice=input("Enter yout choice : ")
        
        if choice=='1':
            listAllVideos()
        elif choice=='2':
            Name=input("Enter the video name : ")
            Time=input("Enter the video name : ")
            addVideo(Name,Time)
        elif choice=='3':
            videoId=input("Enter video ID to update : ")
            Name=input("Enter the video name to update: ")
            Time=input("Enter the video time to update : ")
            updateVideo(videoId,Name,Time)
        elif choice=='4':
            video_Id=input("Enter video ID to delete : ")
            deleteVideo(video_Id)
        elif choice=='5':
            break
        else:
            print("Invalid Choice Selected")
            
    conn.close();

if __name__=="__main__":
    main()