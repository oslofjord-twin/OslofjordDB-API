import { gql } from "@apollo/client";

export const GET_SALINITY_2 = gql`
    query Salinity($date_from: String!, $date_to: String!) {
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
    }
  }
`;

export const GET_TURBDITY = gql`
  query Turbidity {
    turbidity(limit: 10) {
      record_time
      temperature
      turbidity
    }
  }
`;