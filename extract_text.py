#! /usr/bin/env python3


def get_soup(webpage_location):
    '''
    input:  location of a HTML webpage
    output:  html parsed by Beautiful Soup module
    '''

    import bs4

    text = get_webpage(webpage_location)            # function not shown
    soup = bs4.BeautifulSoup(text, 'html.parser')   # parses html

    return(soup)


def extract_text(soup):
    '''
    Extracts text description of image from HTML
    input:  HTML parsed by package Beautiful Soup
    output:  the text description
    '''

    image_text = ''
    image_html = soup.select('div div div div div div div a img')

    try:
        image_text = image_html[0].get('alt')
    except:
        image_text = 'ERROR:  failed to extract text from html'

    return(image_text)


def get_text_from_webpage(webpage_location):
    '''
    input:  location for a HTML webpage
    output:  text description of image from HTML
    '''

    soup = get_soup(webpage_location)
    text = extract_text(soup)

    return(text)


def save_webpage_text_to_table(date_list, webpage_list):
    '''
    input:  list of dates and list of webpage locations
    output:  saves 'csv' file with table of extracted descriptions of images
        (2nd column) and corresponding dates (1st column)
    '''

    import pandas as pd

    message_interval = 100

    text_table = pd.DataFrame(data={'pagename': date_list, 'text': ''})

    for i in range(len(webpage_list)):

        # loop status message
        if (i % message_interval) == 0:
            print('Processing page {0} of {1}, which is {2:.0f}%'
                .format(i + 1, len(webpage_list),
                        100 * (i + 1) / len(webpage_list)))

        text_table.iloc[i, 1] = get_text_from_webpage(webpage_list[i])

    # '^' used as separator because it does not appear in any text descriptions
    text_table.to_csv('table.csv', sep='^', index=False)


def main():
    '''
    Extracts descriptions of images from HTML webpages and saves those
        descriptions in a table in a 'csv' file in the current working directory
    '''
    # webpage for comic dated June 3, 1970 did not have a text description

    date_list, webpage_list = get_webpage_list()    # function not shown

    # extract text descriptions of images from webpages and save them to a
    #       table in a 'csv' file
    save_webpage_text_to_table(date_list, webpage_list)


if __name__ == '__main__':
    main()
