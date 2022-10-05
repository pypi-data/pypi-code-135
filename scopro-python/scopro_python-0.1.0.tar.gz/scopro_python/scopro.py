#!/usr/bin/env python
# coding: utf-8

# In[120]:


import numpy as np
import pandas as pd


# In[412]:


def SCOPRO(norm_vitro_df, norm_vivo_df, cluster_vitro, cluster_vivo, name_vivo, marker_stages_filter, marker_stages, selected_stages, threshold = 0.1, number_link = 1, fold_change = 3, threshold_fold_change = 0.1):

    # check input
    assert(np.sum([selected_stage in name_vivo for selected_stage in selected_stages]) > 0)
    assert(np.sum([cluster in name_vivo for cluster in cluster_vivo]) > 0)
    assert(np.sum([selected_stage in cluster_vivo for selected_stage in selected_stages]) > 0)
    assert(len(marker_stages_filter) > 0)

    mean_stage = get_mean_stage(norm_vivo, cluster_vivo, name_vivo,
                            marker_stages_filter)
    names_vivo = mean_stage.index.values
    connectivity_vivo = find_connectivity(mean_stage, fold_change,
                                         threshold_fold_change)
    return





# In[ ]:
