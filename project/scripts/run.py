from crawler.harvestMode import HarvestSys


def run_crawler(crawler):
    crawler.StreamMode()
    
    # search api have limit access, better use streamMode
    #crawler.SearchMode()

    



if __name__ == '__main__':
    crawler = HarvestSys()
    run_crawler(crawler)
    
