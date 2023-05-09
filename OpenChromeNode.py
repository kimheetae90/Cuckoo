# ExecuteNode를 상속받아서 OpenChromeNode를 만든다
# OpenChromeNode는 execute()를 구현해야 한다

import asyncio
import os
from ExecuteNode import ExecuteNode
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OpenChromeNode(ExecuteNode):
    def __init__(self):
        super().__init__()

    async def execute(self) -> 'ExecuteNode':
        # chrome을 실행한다
        # 크롬 드라이버 경로
        # 현재 파일의 디렉토리 경로
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # chromedriver 경로
        chrome_driver_path = os.path.join(current_dir, 'chromedriver')

        # 크롬 브라우저 옵션 설정
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless') # 창을 띄우지 않고 백그라운드에서 실행

        # 크롬 드라이버 생성
        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

        try:
            # Chrome 브라우저 열기
            driver.get('https://www.google.com')
            # execute 함수를 10초 동안 기다린다
            await asyncio.sleep(10)

        finally:
            # Selenium 드라이버 종료
            driver.quit()

        # chrome을 실행한 후에는 다음 노드로 넘어간다
        return self.next_nodes[0] if self.next_nodes else None