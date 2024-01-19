"use client";
import React from "react";
import { useQuery } from "@apollo/client";
import { GET_SALINITY_TIME_FRAME } from "../queries/gqlQueries"

const ApiCallExample = () => {
    const { loading, error, data } = useQuery(GET_SALINITY_TIME_FRAME, { //set which query to run here with variables
      variables: { date_from: "2023-04-12", date_to: "2023-04-14" },
    });
  
    if (loading) {
      return <div>Loading...</div>;
    }
    if (error) {
      console.error(error);
      return <div>Error!</div>;
    }
    console.log(data);
    return (
      <div>
        <pre>{JSON.stringify(data, null, 2)}</pre>
      </div>
    );
  };
 
export default ApiCallExample;