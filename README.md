# JAVA dat.bin Scripts
Python scripts that extracts files and rebuild dat.bin file from Java Mobile Game like Giana Sisters (and possibly others games sharing this file format).
## Step
1. Extract the dat.bin from the JAR file. JAR are ZIP files, **you can decompress it with File Explorer (if you change its extension) or a tool like 7-Zip**
2. Check the dat.bin throught Hex Editor or NotePad. **It must have the same format as seen in the [txt file](https://github.com/zigaudrey/JAVA-dat.bin-scripts/blob/main/GIANA-dat.bin-file-format.txt).** If not, don't use the scripts
3. Launch the extractor script and choose the dat.bin. **A new folder will be created along with the extracted files**
4. Once you modified the files (not the names), **launch the builder script and choose the folder**
5. **Replace the modded files and compress the folder with the JAR extension instead of ZIP** (don't forget the META-INF folder)
