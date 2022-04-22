ratingPanel = driver.find_element(by=By.ID, value="ratingFormOuterPanel")
            #ratingPanel = driver.find_element(by=By.XPATH, value="//div[@id='ratingFormOuterPanel']")
            rect = ratingPanel.find_element(by=By.XPATH, value="/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]")
            #rect = ratingPanel.find_element(by=By.XPATH, value="//div[2]/div/div/div[3]/div/div/div[1]/div/svg/g[1]/rect")

            
            #rate = ratingPanel.get_attribute("column-id")
            print(num + ": " + rect.tag_name)
        #except:
            print("score not found") 