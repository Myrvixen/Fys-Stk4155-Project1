# Linear Regression analysis   
This is a project comparing the popular linear regression methods Ordinary Least Squares, Ridge and Lasso Regression. All the methods are evaluated first on the famous Franke function, and then on real data from https://earthexplorer.usgs.gov/.

## Build with
scikit-image    0.13.1  
scikit-learn    0.19.2  
pytest          3.2.1   
python          3.6.2  
numpy           1.13.3  
matplotlib      2.0.2   
tqdm            4.23.4      
imageio         2.3.0   

## Structure of the repo
### Documentation
The documentation of class Lin_Reg contained in cls_reg.py was generated using sphinx.  
View documentation by typing   
open doc/_build/html/index.html   
in the terminal   


### Src
 **CV.py:** Running cross validation and bootstrap on franke function   
 **CV_terrain.py:** Running crossvalidation and bootstrap on real data   
 **Bias_variance_ols.py:** Examine the bias vairance trade of      
 **ols.py:** Generating plot of mse vs complexity for ordinary least squares    
 **lasso.py:** Generating heat map of mse as a function of noise and lambda    
 **ridge.py:** Generating heat map of mse as a function of noise and lambd     
 **run_real_data.py:** Generating plots of mse vs degree and mse vs      
 **misc_programs:** Directory contains programs used to generate example plots
 **cls:** Package
 * **split_patches.py:*** Used to split terrain data into random patches of a given size    
 * **plotparams.py:** Parameters for ploting
 * **cls_reg.py:** Class containing linear regression methods ols, ridge and lasso; resampling k-fold and bootstrap; statistics MSE and R2    
 * **unit_test.py:** A few tests to make sure Lin_Reg class is working  
 * **Franke.py:** Generating data from franke function. Also plot if explicitly run.   

### Data
Contains different terrain data. SRTM_data_Norway_1.tif has been used in this project

### Plots
Folder of plots generated. Several not used directly in the project.


## Running the tests
Run unit_test.py with pytest -v  
pytest unitest.py -v



## Authors

* **Tommy Myrvik** - (https://github.com/Myrvixen)
* **Kristian Tuv** - (https://github.com/kristtuv)
