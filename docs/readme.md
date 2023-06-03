# Class diagrams

## Estimator
![Alt text](http://www.plantuml.com/plantuml/png/lLDTIyCm57tlhxZC1pzmWxqM7uPR5HzMP0CHH2Hcjnf8cv5xzo1p_zsqMudjCYk8UydMctFFERad6H4BowjSHwSmmKmLYfKf83CMvj9Oj7S5eys4n4ZL_zexi8u0rkALs0h96w1o--myXeMI_EIgbv1f8_WvsaIHr888nkMgCYL5ARVb0vKlDUPOC0KLxYrAHGuUR-bSQOPIQEs_RuOlLQUlZAqXIWgsPldXgpk7tiyCtomI_ThBT9u4sThOgy_187ZOCB9j8zfF9I5MkM0J3AQnwTsUB0IB62PkzLskJ9L8l9Tq8yrCiJjRexIqM4RxVO3pXsbzpERq3bYgMJqLG6qdD2-lz7XxRGpnaTJIz4X2YLjPoHHvTmdCN_LsF8T7-9z2JHf_mnltv23APzo5JDDkK6YsNT8_0dl37bpq-zLlw-t4y2u8H4TNzHJtUaPOB5Qv_W80 "Estimator")


## Dataset
Creating a good abstraction for our data may be the most important part of this project, because this is probably the biggest reason for the incompatibility between different frameworks, as well as the tight coupling of different components even *within* some of the major ML frameworks (example of AWS Sagemaker coming soon).

### Interfaces
Let's start by defining the *interface* we will implement. Actually, this is split into two different interfaces to account for the two different kind of operations we want to perform, splitting and transforming between different formats:
![Alt text](http://www.plantuml.com/plantuml/png/ZPBHQeDG38RlprFaKZVm0KIaR6Emwps0P3Ps1uxdbEHtDslVVTfsTb1nlPAOp_p9Xni3AuO-EESZH3jkXPxOv8N1poc2VHHzcrlVZkYngbeLXjHrfwblRFWmWMNvGgzD_Ju8f37124p4Jj10sSTco-0iB-UyTy6SD9DYk0lyuk17pgVxvd88wzpHkJQmsQqDj-AdEXJ5xHTKafyyz19Xz4VrOlIIuovfpyZEZ-l6hwVwx1NfF-fokY4fx-INFhtVYvgtgJWwjtPWKHpgnQrB6aoCiYdXuQAML31eDFBHmB4T-_XaN6KiJigTsqZSJZ_b3m00 "data_container_interfaces")

The BaseData*Container*Interface provides a contract for how we can get relevant subsets (training, test, and validation set), as well as the whole data set, from our data abstraction.(Note that it does not contain a method to split the data, because this can be handled by our data abstraction under the hood *if* necessary - and it will in fact not always be necessary, because we should allow our data container to be constructed from data that already comes pre-split.)

Also note that we will leave it up to the implementation whether the data container "has a " training set, validation set, and test set, or whether it simply "has a" single/combined dataset and returns the relevant subsets when requested. The data container interface simply provides a contract for:
- how we should be able to retrieve the subsets (as well as the complete data set);
- that we should be able instantiate it both by giving it the complete data set, as well as by giving it the individual subsets (in case our data set has already been split).

Now let's talk about the second interface, the BaseDataSetInterface. It provides a contract for the kind of objects that our data container returns: Both the complete data set as well as its subsets will implement the BaseDataSetInterface. Its main purpose is to decouple our dataset abstraction from the specific way this data is represented (whether in persistent storage or in-memory). To that end, it contains two important methods:
- a constructor, that takes as its argument the data format from which to instantiate the data set;
- a to_format() method, which allows us to access the data in the format thatwe supply as the argument.

But how do we constrain the permissible data formats to only those that make sense were given kind of data? To model this, we actually will not implement the BaseDataSetInterface directly, but rather we will derive more specific interfaces to model the kind of data sets we are dealing with:

![Alt text](http://www.plantuml.com/plantuml/png/dPJ1Rk8m48RlVeevWdRX0L0KaTqaAXMbBGczHXPCqaWaGVRaK1NUlPgK6e4oBVHasVw_yJ-_HfvQqeRQQgjKMHEQNAyH_ccBeIQT8CtSuRi2-EDvQuEQqFTpqrHPtfXAq-1pcJWkxlP31gYvGbGWPPOQemlyKdVdEpIsjBmvADLhojkFHf2GQTVK6jpmlRlyZi2gl9sAoosUQq-PIIQkYUqCbSEJfOSp8zpRhyquN3OaosLJ7DtDLXYI7tS2zrnVryAGM2Gb1oLE2MEkbVxXO8bIMBVLnQI3vy4W-biOn7e84GjylujXjGYZUBQ8GdKuads9olnJi7nUHQa2-9-yA83xv74nv_Cm2uCqY9V1G-HASrEtbU_AEPxx_DbGUdTSilaiIHc-38Cpw_FH9nHC2-AJG-7J69koUANnteSBV0AjHGk33UPbZHOCKcjgeBST3fMQOhtXZ_83 "dataset_interface_simplified")

We use an Enum to model the possible datatypes that a given type of data could be represented. For example, a structured data set would be commonly stored on disk in a parquet, csv, or JSON Lines format, or in memory as a Pandas DataFrame. (Note that you should return format will correspond to a given return type which is not necessarily the same. For example, when we get our dataset in csv format the return type would be `str`, or even `None` if we write to a file . We will deal with these details later).

For simplification, the previous diagram omitted the relationship between the specific interfaces and the corresponding enum; the more complete diagram would look like this:

![Alt text](http://www.plantuml.com/plantuml/png/bPJ1Re9048Rl-nHxrBJw08OGQO7KnjfMi5UoqO6I29ZTuT1KtxqkjKmq3A4NSNV_R_QVFvET6rGQws8lH5uYw5HjGJue0xv25G4ksirl8UMTusmrA0JNJNLL96cb2uMZty-ivS9cFRO0LWD46M1YiD8gWpzrity0RN9Z5oSXEaqvnyb4HgZhBTOQTlQyFUmZeCZ_JuNv7gwrb1bZOb1iXBBXzKjFLqRutWQP8PmtnCiPKnJTS2iDn5rE0hgEwxfZI0oWO8FYfyHYr4hdS5Y9453MnSsaIyUHe-0-qm3bM0PMuBfD39kL7uIBLU2BquMaMuVmRzxwVHF4vt-FqSVvzpbwNItjlf_uNko5Q-ybeDBKrC3oJRcMfypx3CLFbq-oN4InXM_3i9br-UWICgOPCJba7esfphDFd1vTUOFFP6t0oD4Eqhm48pLWhKk9NmSOy-D5vJejalS-b6_HjiDGLwtEeTpPT_m7 "dataset_interface")

### Implementation
Here is my proposal for how to implement the above interfaces: Our *container* class will "have a" data splitter object (which contains concrete logic for how to split the data into training, validation, and test set, and uses information about the dependency relationship between the individual records to carry this out properly):
![Alt text](http://www.plantuml.com/plantuml/png/nPH1Rzim38Nl-XL4JYs66DsEGHOKwr1Wv-nkS3RJ2P0bWwHtMVlV9qTTd47CaEtIInAJtxFUendVYoBhD0Jd77uJPUmKke0Yy0c5FgFYGugAFXB3JmVmRhljc51fjpjm6jf3uW7rfdnjJgB7u_NjBD1q1VH4seecnYVwJH_h8x5uAHTha35uLUBb5llNYdkn_Iz8iRy69T5sv3GcLf_Y1WuXeS97k6i-784V67oFS--lM7iqqsOIYrMOCoYZZrMHf09FfvpedA0O_n9x6Yb_HFqZOkb-zGFjYJs95IutMpyh_S4JotBJXp19vgWtL5tfsSBzYEenMBAKkFSHjJgo6ltsURs-cCkcxPmsRAUpMIkGkxmyf6-xzdcQzHznzNu5AKTPtJLD_bdbtC1t5413sJJFk_Dm6Ps416uwZC2a4yVRqvDNdhfSeVuLlc8GYyOOnpNeidSq-FzmOEXi5pPkENdquLzsOSRj8mtWnPqzZBAVLUWACKnRsBbnv-ufzlDx_XS0 "dataset_implementation")


# Pipeline
Finally, here is a complete ML pipeline:
![Alt text](http://www.plantuml.com/plantuml/png/XP91ImCn48Nl-ok6dbIeuBMd8kfDASLx6RFZDZIRX9afMCJ_RhAfeTlAzXJoyhsypPjTYYBhldUDSIW2Anl9MK_mtG3mtj_SBk0jU6f-cZ-2QSN1a4ZWWOfCiGWPVaB55yR-nF4iQdlK8_vfDNEleILNtAqrW-JZFJBZ8QbY0jDmNJexoGwYP-59kPB-5ObjJrxV6SsEYi-5hZuDe2FT94Kk4ijdhgcpedmefGmRuZDxdy7wi56yG-kFiLHscLjJ3An9Criokys7nI7-CQtbADzHnp5xcC7TV9xNyGGMi4K1_9-ipKzZuredqSis9_5nVPDeBQfYI_9j_ZD_0G00 "Pipeline")
Note that this is part of the design is lowest priority, because there already exist a number of good pipeline tools such as MLFlow Piperlines. Thus, I still need to decide if the pipeline abstraction is even needed.
