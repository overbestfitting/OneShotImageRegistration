import torch
#
#general options
#
useContext = True
debugMode=True
handleStructsAsImages=True
numberOfEpochs = [1000,1000,1000]#[300,200,1000]#for ecomp paper
#numberOfEpochs = [200,250,1000]#with training of 3D pairs
trainingFileNamesCSV=''
device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
outputPath='.'

netDepth=3
numberOfFiltersFirstLayer=32
netMinPatchSizePadded = 8
patchSize=(80,80,80)
netMinPatchSize = patchSize[0]
normImgPatches=False
trainTillConvergence = True
ccCalcNN=True
maskOutZeros=False
useMedianForSampling = (False,False,True)

#
#cost functon parameters
#
ccW=0.5
dscWeight=0.5
downSampleSteps = 1# a size of 2 means 3 iterations with the following downsampling factors: (0.25,0.5,1.0)
stoptAtSampleStep=2
boundarySmoothnessW=(0.0,0.1,0.1)
smoothW = (0.0005,0.0005,0.0005)
cycleW = 0.01
lossTollerance=0.00001#0.00001#0.0000001#
valueToIgnore=-1000#None #set values outside mask to this value and ignores them during optimisation

#
#difeomorphic version parameters
#
diffeomorphicRegistration = True
overlappingPatches=True
finalGaussKernelSize=7
finalGaussKernelStd=2
sasSteps=5
smoothVF = True #if true then the smoothness function of smoothW loss is used


#
#training parameters
#
validationIntervall=10
# numberOfEpochs = [75,75,75]
addVectorFields=False
fineTuneOldModel=(False, False, False) # works only in combination with "previousModels" parameter
randomSampling=(False,False,False)




