## Information ADDED for PARENT DATASET
# SiStrip Det. ONLY
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_Performance
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTECB_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTECB_OnlineDQM
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTECB_Performance
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTECF_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTECF_OnlineDQM
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTECF_Performance
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTIB_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTIB_OnlineDQM
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTIB_Performance
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTIDB_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTIDB_OnlineDQM
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTIDB_Performance
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTIDF_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTIDF_OnlineDQM
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTIDF_Performance
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTOB_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTOB_OnlineDQM
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=GOOD --tag=SiStrip_SummaryTOB_Performance
#
# Lets see if the info is diplayed correctly
python listDQ.py --run=1111 --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM
#
# SAME DQ is inherited by the CHILD Dataset
python listDQ.py --run=1111 --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW
#
# NOW, lets ADD MORE info to CHILD-ONLY
# PIXEL Det. ONLY
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_Performance
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryBarrel_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryBarrel_OnlineDQM
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryBarrel_Performance
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryEndcap_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryEndcap_OnlineDQM
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryEndcap_Performance
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryHCmI_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryHCmI_OnlineDQM
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryHCmI_Performance
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryHCmO_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryHCmO_OnlineDQM
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryHCmO_Performance
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryHCpI_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryHCpI_OnlineDQM
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryHCpI_Performance
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryHCpO_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryHCpO_OnlineDQM
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryHCpO_Performance
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryShellmI_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryShellmI_OnlineDQM
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryShellmI_Performance
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryShellmO_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryShellmO_OnlineDQM
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryShellmO_Performance
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryShellpI_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryShellpI_OnlineDQM
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryShellpI_Performance
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryShellpO_Global
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryShellpO_OnlineDQM
python setDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=GOOD --tag=Pixel_SummaryShellpO_Performance
#
#  The CHILD DATASET will have BOTH Parent-DQ and Its own DQ (SiStrip + Pixel)
python listDQ.py --run=1111 --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW
#
# While Check Again that Parent ONLY has the SiStrip
#
python listDQ.py --run=1111 --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM
#
# Now lets update some of Child Dataset's DQ Flags and See if updated results are visible. (MIND that so far ALL were GOOD lets put some of them as BAD)
python updateDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --run=1111 --value=BAD --flag=Pixel_SummaryShellpO_Performance
#
### Verify the Parent flags are unchanged and Child Flags are changed as required.
# List Parent
python listDQ.py --run=1111 --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM
# List Child
python listDQ.py --run=1111 --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW
#
#Now lets update one of Parent Dataset Flag and See if its show changed in BOTH Parent and Child
python updateDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=BAD --flag=SiStrip_SummaryTOB_Performance
#
#
# List Parent
python listDQ.py --run=1111 --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM
# List Child
python listDQ.py --run=1111 --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW
#
# Lets VERSION this information as v00_00_11
#
python dqVersion.py
#
#List parent and child DQ for this version
python listDQ.py --dqversion=DQ_00_00_11 --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM
python listDQ.py --dqversion=DQ_00_00_11 --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW
#
# Lets update Parent and Child FLAGS and list 
#
# Parent flag
 python updateDQ.py  --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM --run=1111 --value=UNKNOWN --flag=SiStrip_SummaryTECB_OnlineDQM
# Child-Only flag
python updateDQ.py  --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW --value=UNKNOWN --flag=Pixel_SummaryBarrel_OnlineDQM --run=1111
# List Parent
python listDQ.py --run=1111 --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM
# List Child
python listDQ.py --run=1111 --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW
#
#
# Lets list TAGed version again to see that nothing changed there
python listDQ.py --dqversion=DQ_00_00_11 --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM
python listDQ.py --dqversion=DQ_00_00_11 --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW
# Lets adda DUPLICATE FLAG in Child (Already present for the Parent, we must only get Child Flag when listing
python setDQ.py --run=1111 --value=BAD --tag=SiStrip_SummaryTOB_OnlineDQM --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW
# List Child 
python listDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW
# List Parent to verify nothing changed there
python listDQ.py --dataset=/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM



