
from keep_alive import keep_alive
keep_alive()
import time


# تعيين المتغير flag على True
flag = True

while flag:
    try:
        # قراءة وتنفيذ الملف main1.py
        exec(open("main1.py").read())
    except Exception as e:
        print(f"حدث خطأ في main1.py: {e}")
        # استمرار التنفيذ بدون إيقاف البرنامج

    try:
        # قراءة وتنفيذ الملف main2.py
        exec(open("main2.py").read())
    except Exception as e:
        print(f"حدث خطأ في main2.py: {e}")
        # استمرار التنفيذ بدون إيقاف البرنامج

    try:
        # قراءة وتنفيذ الملف main3.py
        exec(open("main3.py").read())
    except Exception as e:
        print(f"حدث خطأ في main3.py: {e}")
        # استمرار التنفيذ بدون إيقاف البرنامج
    try:
        # قراءة وتنفيذ الملف main4.py
        exec(open("main4.py").read())
    except Exception as e:
        print(f"حدث خطأ في main4.py: {e}")
        # استمرار التنفيذ بدون إيقاف البرنامج

    time.sleep(0.001)

# الأكواد هنا تعمل عندما يتم إيقاف الحلقة
print("Stopping the program")
