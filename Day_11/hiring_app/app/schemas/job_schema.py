from pydantic import BaseModel, ConfigDict

class JobBase(BaseModel):
    title: str
    description : str
    salary : float
    company: str

class JobCreate(JobBase):
    pass 

class JobUpdate(JobBase):
    title : str | None = None
    des : str | None =None
    salary : float | None = None
    company : str | None = None

class JobResponse(JobBase):
    id : int
    # class Config:
    #     form_attributes = True
    model_config = ConfigDict(form_attributes = True)
'''
JobBase - Contains the common fields shared by all jobs
JobCreate - Used when creating a new job
JobUpdate - Used when updating the job
All fields are optional
JobResponse - Used when sending jobs details back to the client.
Includes the generated id
'''