plb_data
==============================
[//]: # (Badges)
[![codecov](https://codecov.io/gh/dfhahn/plb_data/branch/master/graph/badge.svg)](https://codecov.io/gh/dfhahn/plb_data/branch/master)


Data for benchmarking protein-ligand binding free energy calculations. 

### File tree and file description

The data is organized as followed:  

```
plb_data
├── targets.yml                               # list of all targets and their directories   
├── <date>_<target_name_1>                    # directory for target 1
│   ├── 00_data                               #     metadata for target 1
│   │   ├── edges.yml                         #         edges/perturbations
│   │   ├── ligands.yml                       #         ligands and activities
│   │   └── target.yml                        #         target
│   ├── 01_protein                            #     protein data
│   │   ├── crd                               #         coordinates
│   │   │   ├── protein.pdb                   #             aminoacid residues   
│   │   │   └── cofactors_crystalwater.pdb    #             cofactors and cyrstal waters    
│   │   └── top                               #         topology(s)
│   │   │   └── amber99sb-star-ildn-mut.ff    #             force field spec.           
│   │   │       ├── topol.itp                 #                 Gromacs ITP file
│   │   │       └── topol.top                 #                 Gromacs TOP file
│   └── 02_ligands                            #     ligands
│   ├── lig_<name_1>                          #          ligand 1 
│   │   ├── crd                               #              coordinates
│   │   │   └── lig_<name_1>.sdf              #                  SDF file
│   │   └── top                               #              topology(s)
│   │       └── openff-1.0.0.offxml           #                  force field spec.       
│   │           ├── fflig_<name_1>.itp        #                      Gromacs ITP file : atom types     
│   │           ├── lig_<name_1>.itp          #                      Gromacs ITP file       
│   │           ├── lig_<name_1>.top          #                      Gromacs TOP file                
│   │           └── posre_lig_<name_1>.itp    #                      Gromacs ITP file : position restraint file  
│   ├── lig_<name_2>                          #         ligand 2                               
│   …                                        
│   └── 03_hybrid                             #    edges (perturbations)
│   ├── edge_<name_1>_<name_2>                #         edge between ligand 1 and ligand 2   
│   │   └── water                             #             edge in water 
│   │       ├── crd                           #                 coordinates 
│   │       │   ├── mergedA.pdb               #                     merged conf based on coords of ligand 1  
│   │       │   ├── mergedB.pdb               #                     merged conf based on coords of ligand 2   
│   │       │   ├── pairs.dat                 #                     atom mapping                  
│   │       │   └── score.dat                 #                     similarity score         
│   │       └── top                           #                 topology(s)       
│   │           └── openff-1.0.0.offxml       #                     force field spec.         
│   │               ├── ffmerged.itp          #                         Gromacs ITP file  
│   │               ├── ffMOL.itp             #                         Gromacs ITP file   
│   │               └── merged.itp            #                         Gromacs ITP file     
│   …                                        
├── <date>_<target_name_2>                    # directory for target 2  
…
```


### Copyright

Copyright (c) 2020, Open Force Field, David Hahn


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.4.
