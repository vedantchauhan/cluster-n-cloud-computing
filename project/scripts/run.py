from crawler.harvest import HarvestSys


def run_crawler(crawler):
    crawler.harvest()
    #crawler.searchById("jiyu","869111488388022272")
    # search api have limit access, better use streamMode
    #crawler.SearchMode()

    



if __name__ == '__main__':
    crawler = HarvestSys()
    run_crawler(crawler)
    
