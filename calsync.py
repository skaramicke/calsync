from google_calendar import google_calendar_handler
from icloud_calendar import icloud_calendar_handler


def sync():
    # Load future events from icloud
        # for item in items
            # if item is synced before and if item doesnt exist in google
                # remove item from icloud
            # if item is not synced before
                # if item does not exist in google
                    # create item in google
                # set item as synced in both icloud and google
    # Load future events from google
        # for item in items
            # if item is synced before and if item doesnt exist in icloud
                # remove item from google
            # if item is not synced before
                # if item does not exist in icloud
                    # create item in icloud
                # set item as synced in both google and icloud
    pass

