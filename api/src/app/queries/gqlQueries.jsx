import { gql } from "@apollo/client";

// Add position 
export const GET_SALINITY_TIME_FRAME = gql`
    query Salinity($date_from: timestamptz!, $date_to: timestamptz!) {
      salinity(where: {record_time: {_gte: ,$date_from _lte: $date_to}}) {
        record_time
        temperature
        conductivity
      }
    }
  `;

export const GET_SALINITY = gql`
  query Salinity {
    salinity(limit: 10) {
      record_time
      temperature
      conductivity
      location
    }
  }
`;

export const GET_TURBDITY = gql`
  query Turbidity {
    turbidity(limit: 10) {
      record_time
      temperature
      turbidity
      location
    }
  }
`;