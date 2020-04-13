from django.test import TestCase
import time
# Create your tests here.
order_data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print(order_data)
