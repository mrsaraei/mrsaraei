from scholarly import scholarly
import pybadges
import os

# Replace with your Google Scholar ID
USER_ID = "IwY5S7kAAAAJ"

# Get author info
author = scholarly.search_author_id(USER_ID)
author = scholarly.fill(author, sections=['basics', 'indices'])

# Extract total citations
citations = author['citedby']

# Generate badge
badge_svg = pybadges.badge(
    left_text="Google Scholar",
    right_text=str(citations),
    right_color="blue",
)

# Save to file
output_path = "assets/badges/scholar_badge.svg"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w") as f:
    f.write(badge_svg)
