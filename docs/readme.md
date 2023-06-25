# Class diagrams

## Estimator

![Alt text](http://www.plantuml.com/plantuml/png/lLDTIyCm57tlhxZC1pzmWxqM7uPR5HzMP0CHH2Hcjnf8cv5xzo1p_zsqMudjCYk8UydMctFFERad6H4BowjSHwSmmKmLYfKf83CMvj9Oj7S5eys4n4ZL_zexi8u0rkALs0h96w1o--myXeMI_EIgbv1f8_WvsaIHr888nkMgCYL5ARVb0vKlDUPOC0KLxYrAHGuUR-bSQOPIQEs_RuOlLQUlZAqXIWgsPldXgpk7tiyCtomI_ThBT9u4sThOgy_187ZOCB9j8zfF9I5MkM0J3AQnwTsUB0IB62PkzLskJ9L8l9Tq8yrCiJjRexIqM4RxVO3pXsbzpERq3bYgMJqLG6qdD2-lz7XxRGpnaTJIz4X2YLjPoHHvTmdCN_LsF8T7-9z2JHf_mnltv23APzo5JDDkK6YsNT8_0dl37bpq-zLlw-t4y2u8H4TNzHJtUaPOB5Qv_W80 "Estimator")

## Dataset

Creating a good abstraction for our data may be the most important part of this project, because this seems to be the biggest reason for the incompatibility between different frameworks, as well as the tight coupling of different components even *within* some of the major ML frameworks ([the worst of which I encountered with AWS Sagemaker](https://github.com/tloeber/email-classification#lessons-so-far)).

### Interfaces

Let's start by defining the *interfaces* we will implement. Actually, this is split into two different interfaces to account for the two different kind of operations we want to perform: *transforming between different formats*, and *splitting* the overall data. We will think of the former as simply the actual **DataSet** with which we will we working with, and the latter as a **container** for DataSets, because it contain the seperate subsets for training, validation, and testing. Let's first start by looking at this design using a basic visualization:
![Alt text](../img/data_design.jpg)

Here is the more detailed UML diagram:
![Alt text](http:////www.plantuml.com/plantuml/png/ZPD1ReD034NtSmelYLfnW2YAehQgr7KFW5mmwKZ3J6H_kcbwzsQ20fL2Q5R8pBFvtv_P6LZHTy4v7o7QSYtqn2Ol37vE4UoZwDjuzEs87ZQRMeKXssshgQki_p215T0JN9bWFKvu5uozZ_J5mJSCdnOfYE7s-Mf6G9swGn18xYh6Oc54dh4NL8FYXi75QfuTIJ7S1KuUxy8vX6NknxawiDbrA6uXfisnBAyxQ4q-BwUJ2FiJ-EoNvv9katQCOdXCWb_FzR1Mf7-eYtD3KjxBXJw_FuYQjrEHRI_vAylZTbRrcdeJesAGtL2MJHmRKa6lqSX70yTQZF39cFPnwq_PIMpozVW5 "data_container_interfaces")

The BaseData**Container**Interface provides a contract for how we can get the relevant subsets (training, test, and validation set), as well as the whole data set, from our data abstraction. (Note that this interface it does not contain a method to split the data, because this task can be handled by our data abstraction under the hood *if* necessary - and it will in fact not always be necessary, because we should allow our data container to be constructed from data that already comes pre-split.)

Also note that we will leave it up to the implementation whether the data container "has a" (is a composition or aggregation of) training set, validation set, and test set; or whether it simply "has a" single/combined dataset and fetches  the relevant subsets when requested. Our data container interface simply provides a contract for:

- how we should be able to *retrieve the subsets* (as well as the complete data set);
- that we should have the option to *instantiate the data container* both from the *complete* data set, or from the *individual subsets* (in case our data set has already been split).

Now let's talk about the second interface, the Base**DataSet**Interface. It provides a contract for the kind of objects that our data container returns: Both the complete data set as well as its subsets will implement the BaseDataSetInterface. *Its main purpose is to decouple our dataset abstraction from the specific way this data is represented (whether in persistent storage or in-memory)*. To that end, it contains two important methods:

- a *constructor*, which takes as its argument the data *format* from which to instantiate the data set;
- a to_format() method, which allows us to *access* the data in the *format* that we supply as the argument.

This raises the question how we can constrain the permissible data formats to only those that make sense for a given kind of data? To model this, we actually will not implement the BaseDataSetInterface directly; instead, we derive more *specific* interfaces to model the *particular kind* of data sets (e.g., tabular) we are dealing with:

![Alt text](http://www.plantuml.com/plantuml/png/dPJ1Rk8m48RlVeevWdRX0L0KaTqaAXMbBGczHXPCqaWaGVRaK1NUlPgK6e4oBVHasVw_yJ-_HfvQqeRQQgjKMHEQNAyH_ccBeIQT8CtSuRi2-EDvQuEQqFTpqrHPtfXAq-1pcJWkxlP31gYvGbGWPPOQemlyKdVdEpIsjBmvADLhojkFHf2GQTVK6jpmlRlyZi2gl9sAoosUQq-PIIQkYUqCbSEJfOSp8zpRhyquN3OaosLJ7DtDLXYI7tS2zrnVryAGM2Gb1oLE2MEkbVxXO8bIMBVLnQI3vy4W-biOn7e84GjylujXjGYZUBQ8GdKuads9olnJi7nUHQa2-9-yA83xv74nv_Cm2uCqY9V1G-HASrEtbU_AEPxx_DbGUdTSilaiIHc-38Cpw_FH9nHC2-AJG-7J69koUANnteSBV0AjHGk33UPbZHOCKcjgeBST3fMQOhtXZ_83 "dataset_interface_simplified")

We use an Enum to model the possible datatypes that a given type of data could represent: For example, a structured data set would be commonly stored on disk in parquet, csv, or JSON Lines format, or in-memory as a Pandas DataFrame. (Note that the *type in Python* corresponding to a given return format is not necessarily the same: For example, when we get our dataset in csv format, the return type would be `str`, or even `None` if we write to a file. We will deal with these details later).

For simplification, the previous diagram omitted the relationship between the specific interfaces and the corresponding enum; the more complete diagram would look like this:

![Alt text](http://www.plantuml.com/plantuml/png/bPJ1Re9048Rl-nHxrBJw08OGQO7KnjfMi5UoqO6I29ZTuT1KtxqkjKmq3A4NSNV_R_QVFvET6rGQws8lH5uYw5HjGJue0xv25G4ksirl8UMTusmrA0JNJNLL96cb2uMZty-ivS9cFRO0LWD46M1YiD8gWpzrity0RN9Z5oSXEaqvnyb4HgZhBTOQTlQyFUmZeCZ_JuNv7gwrb1bZOb1iXBBXzKjFLqRutWQP8PmtnCiPKnJTS2iDn5rE0hgEwxfZI0oWO8FYfyHYr4hdS5Y9453MnSsaIyUHe-0-qm3bM0PMuBfD39kL7uIBLU2BquMaMuVmRzxwVHF4vt-FqSVvzpbwNItjlf_uNko5Q-ybeDBKrC3oJRcMfypx3CLFbq-oN4InXM_3i9br-UWICgOPCJba7esfphDFd1vTUOFFP6t0oD4Eqhm48pLWhKk9NmSOy-D5vJejalS-b6_HjiDGLwtEeTpPT_m7 "dataset_interface")

### Implementation

Here is my proposal for how to implement the above interfaces: Our *container* class "has a" data splitter object (which contains concrete logic for how to split the data into training, validation, and test set, and uses information about the dependency relationship between the individual records to carry this out properly), as well as how to retrieve each of these subsets. By using an aggregation relationship, the splitter class is easily reusable. In particular, a given splitter can be used for different data sets: For example, the logic for performing a time-series split is the same for a structured dataset and an image dataset.

Note that we even require this splitter to be present in the case where the data already comes pre-split. Here, it still performs the important job of  retrieving the relevant subsets (including the whole data set). Note also that this PreSplitDataSplitter will indeed implement the _split_data() method to satisfy the common interface, but since it should never be called, this method will always raise a (semantic) error.

![Alt text](http:////www.plantuml.com/plantuml/png/lPP1RzGm48NFpQ_miHLaXJYkIbKeL0A9WXea3WX5qtXsQocne_44L57-E_6acqJPsHPnu99TUxvdFp_RcpsF3CHTKsVP6uZu5XWkWcTm7ic4F3UxtgAj7JEIMPjRY0RCiSKQjy0O3OSJHRqYjxtbrVtPD0PoB-zYBpckWezCNSLepOP2Oy1RGyWT-NYIPN3JLw5YKzKGezaV_LTcpBFJqueG6C_EqX3b9b03V3nyh4VHfRHFae33Nq1Rv39o8DZYZfR-5Ycwc1g_TODJJ8E_t316BbiARI1smQ_DfWx0vfLviNefm0-edOLKUnGhOngtx4aOl9XaaWcSt-l4k0TEimmLMS5W_Bsts6B_y3pt_r3zuXeia1n6RN5ziNH9wJOEAVQ33ggBkeizXbOHLKDDrHKji8DQKuL0rdbWVSBFX2AOAmUXHEJyjep8Yy37BabC6ikarwR01ZoxwXrH8Ccp2isDypWBSc_lJ-_p_62mEgq7hSDwlZghPQgJQeZPuOEE_B0tX62HffjqBMqf_IJ7yz9NQV__cvii3j_4aNQ35_PbRODitM_bHsm2tLrZInZHivoVwVI1jn17tL6IhKrhL-AEeC4H_L1ykbg2rbNyxRM_UsxwntVTsPIUE1k2JTQkWiSacJiPkICT4nSBQ4Bc6npoV9cB_lElg2RFXrNPOd0vX_CuLM0ACSiMyqXzde8AJElV9LB8gwZRNIdafryl2ysZHrL5f_qei77_u43HwIvqN7DowUfn6vys8BWwfG8ipfRin7xk2h9qhMCpvrbsZjwc_pH_0000 "data_container_implementation")

# Pipeline

Finally, here is a complete ML pipeline:
![Alt text](http://www.plantuml.com/plantuml/png/XP91ImCn48Nl-ok6dbIeuBMd8kfDASLx6RFZDZIRX9afMCJ_RhAfeTlAzXJoyhsypPjTYYBhldUDSIW2Anl9MK_mtG3mtj_SBk0jU6f-cZ-2QSN1a4ZWWOfCiGWPVaB55yR-nF4iQdlK8_vfDNEleILNtAqrW-JZFJBZ8QbY0jDmNJexoGwYP-59kPB-5ObjJrxV6SsEYi-5hZuDe2FT94Kk4ijdhgcpedmefGmRuZDxdy7wi56yG-kFiLHscLjJ3An9Criokys7nI7-CQtbADzHnp5xcC7TV9xNyGGMi4K1_9-ipKzZuredqSis9_5nVPDeBQfYI_9j_ZD_0G00 "Pipeline")
Note that this is part of the design is least mature and lowest priority, because there already exist a number of good pipeline tools such as MLFlow Piperlines. Thus, I still need to decide to what extent the pipeline abstraction is even needed. However, a good *data* abstraction - which I am first focusing on developing – will be key in order to have minimal coupling between pipeline components. For example, this is not only necessary to decouple the preprocessor from the estimator, but also so we can easily re-use model quality evaluation (accuracy, etc.) and explainability tools.
