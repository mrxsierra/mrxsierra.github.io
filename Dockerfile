FROM squidfunk/mkdocs-material AS build
WORKDIR /docs
# Install dependencies from requirements.txt
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# Install additional plugins
# RUN pip install mkdocs-macros-plugin
# RUN pip install mkdocs-glightbox
RUN pip install mkdocs-blogging-plugin
RUN pip install mkdocs-git-revision-date-localized-plugin

# Final dev build
FROM build AS dev