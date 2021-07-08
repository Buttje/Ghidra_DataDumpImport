# Loads a file from disk as binary data to memory that already needs to exists in the Ghidra project
#@author Lutz Pape lutz.pape@gmail.com
#@category fish4tools
#@keybinding 
#@menupath 
#@toolbar

# License: GPLv3

from ghidra.program.model.data import Structure, StructureDataType, UnsignedIntegerDataType, DataTypeConflictHandler
from ghidra.program.model.data import UnsignedShortDataType, ByteDataType, UnsignedLongLongDataType
from ghidra.program.model.mem import MemoryBlockType
from ghidra.program.model.address import AddressFactory
from ghidra.program.model.symbol import SourceType
from ghidra.program.model.mem import MemoryConflictException

if (currentProgram==None):
    print("Please open the destination program first")
    exit()
    
memory = currentProgram.getMemory()

binary_filename = askFile("Choose the file with the binary data", "Load binary data")
binaryFile=open(str(binary_filename), "rb")
filebytes=binaryFile.read()

address = askAddress("Destination", "address")
block=memory.getBlock(address)
print("Loading bytes to block "+block.getName())
block.setSourceName("Binary Loader")
block.setComment("Loaded by DataDumpImport.py")
if (not(block.isInitialized())):
    print("Hello")
    memory.convertToInitialized(block,0)
block.putBytes(address, filebytes)
print("Done")
