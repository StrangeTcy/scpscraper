# Before we begin, we obviously have to import scpscraper.
import scpscraper

# Grab 000-099 in a format that can be used to train AI
scpscraper.scrape_scps(1, 3, ai_dataset=True, copy_to_drive=False)

