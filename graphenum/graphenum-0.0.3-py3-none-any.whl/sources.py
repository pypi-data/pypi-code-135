"""Manage sources of data for the module."""

import json
from typing import Dict, Optional, Tuple

import aiohttp

INTROSPECTION_QUERY: Dict[str, str] = {
    'query':
        """
query IntrospectionQuery {
  __schema {
    queryType {
      name
    }
    mutationType {
      name
    }
    subscriptionType {
      name
    }
    types {
      ...FullType
    }
    directives {
      name
      description
      locations
      args {
        ...InputValue
      }
    }
  }
}

fragment FullType on __Type {
  kind
  name
  description
  fields(includeDeprecated: true) {
    name
    description
    args {
      ...InputValue
    }
    type {
      ...TypeRef
    }
    isDeprecated
    deprecationReason
  }
  inputFields {
    ...InputValue
  }
  interfaces {
    ...TypeRef
  }
  enumValues(includeDeprecated: true) {
    ...EnumValue
  }
  possibleTypes {
    ...TypeRef
  }
}

fragment EnumValue on __EnumValue {
    name
    description
    isDeprecated
    deprecationReason
}

fragment InputValue on __InputValue {
  name
  description
  type {
    ...TypeRef
  }
  defaultValue
}

fragment TypeRef on __Type {
  kind
  name
  ofType {
    kind
    name
    ofType {
      kind
      name
      ofType {
        kind
        name
        ofType {
          kind
          name
          ofType {
            kind
            name
            ofType {
              kind
              name
              ofType {
                kind
                name
              }
            }
          }
        }
      }
    }
  }
}
"""
}


async def fetch_schema(
    url: str,
    headers: Optional[Dict[str, str]],
) -> Tuple[Optional[Dict], aiohttp.ClientResponse]:
    """Fetch a schema from a URL."""

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=INTROSPECTION_QUERY, headers=headers) as resp:
            try:
                body = await resp.json()
            except aiohttp.ClientError:
                return {}, resp

    data = body.get('data', body)
    assert '__schema' in data, 'Invalid schema'
    return data['__schema'], resp


def load_schema(path: str) -> Dict:
    """Load a schema from a file."""

    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
