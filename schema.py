from sqlalchemy import Integer, Float, String, Column
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# create Engine
engine = create_engine(
                       "postgresql://pranav:password@localhost/un_population",
                       echo=True
                       )

# create Base
Base = declarative_base()


# Countries class
class Countries(Base):
    __tablename__ = "countries"

    country_code = Column(Integer, primary_key=True)
    region = Column(String, nullable=False)

    def __repr__(self):
        return f"Countries(country_code={self.country_code},\
                 region={self.region})"


# Population class
class Population(Base):
    __tablename__ = "population"

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    population_yearwise = Column(Float)
    country_code = Column(Integer, ForeignKey("countries.country_code"))

    country = relationship("Countries", back_populates="population")

    def __repr__(self):
        return f"Population(year={self.year},\
                 population_in_millions={self.population_in_millions})"


Countries.population = relationship(
                                    "Population",
                                    order_by=Population.id,
                                    back_populates="country"
                                    )

Base.metadata.create_all(engine)
