'''
动作链---鼠标拖拽
'''
import time
from selenium import webdriver

from selenium .webdriver import ActionChains

browser = webdriver .Chrome ()

url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
#浏览器屏幕最大化
browser .maximize_window()
browser .get(url)
#切换到子Frame
browser .switch_to_frame('iframeResult')
#source: 要拖拽的节点，target: 拖拽到目标节点
source = browser .find_element_by_css_selector('#draggable')
target = browser .find_element_by_css_selector('#droppable')

#浏览器实例化一个动作链
actions = ActionChains (browser )
#调用drag_and_drop方法拖拽
actions .drag_and_drop(source ,target )
#执行拖拽动作
actions .perform()

time.sleep(5)
browser .close()