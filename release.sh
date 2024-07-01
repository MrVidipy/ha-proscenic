#Script to create the release.zip

# Clean the dist directory
RELEASE=release

rm -vR $RELEASE
mkdir $RELEASE

# zip the proscenic sources
cd custom_components/proscenic; zip -r ../../$RELEASE/proscenic.zip . -x "__pycache__/*"