import sys,re
#from datetime import date
#import time
#from selenium import webdriver
#from selenium.webdriver.common.by import By
import requests,os
#from timeout_decorator import timeout
import threading,time

#l1=[10, 16, 29, 32, 41, 43, 56, 57, 88, 96, 106, 122, 131, 186, 189, 208, 258, 273, 277, 284, 286, 287, 289, 290, 293, 296, 297]
#list_300=[300, 301, 302, 304,305,306,307,308,309,310,312,313,314,315,316,318,320,321,323,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,353,355,356,370,371,373,378,381,382,384,386,387,390,398]
# Replace with the URL of the video file you want to download


def test(i,fp):
    video_url = f'http://ser1.desixclip.com/fl/1/{i}.mp4'
    #video_url = 'https://example.com/video.mp4'
    print(f"downloading the {i} file ")

    # Send a GET request to the video URL
    try:
        response = requests.get(video_url)        
        # Check if the request was successful
        if response.status_code == 200:
            # Specify the local file path where you want to save the video
            local_file_path = os.path.join('D:\\abc',f'{i}.mp4')

            # Open the local file in binary write mode and write the video content to it
            with open(local_file_path, 'wb') as video_file:
                video_file.write(response.content)

            print(f'Downloaded {i} file')
        else:
            fp.writelines(str(i)+",")
            print(f'Failed to download video. Status code: {response.status_code}')
    except Exception:
        print(f"connection issue for {i} file")
        fp.writelines(str(i)+",")
        


f= open('D:\\abc\\result.txt','w')      
f.writelines("[")


for i in range(483,600):
    # Set the maximum execution time (in seconds)
    max_execution_time = 420  # 7 minutes

    # Create a thread to execute the function
    execution_thread = threading.Thread(target=test,args=((i,f)))
    
    # Start the thread
    execution_thread.start()
    
    # Wait for the thread to complete or timeout
    execution_thread.join(timeout=max_execution_time)
    
    # If the thread is still running, stop it
    if execution_thread.is_alive():
        print("Execution exceeded 7 minutes. going to next value")
        f.writelines(str(i)+",")
        execution_thread.join()  # Ensure the thread is terminated
        

f.writelines("]")
f.close()