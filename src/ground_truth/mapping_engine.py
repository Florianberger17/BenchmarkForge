"""
BenchmarkForge - Mapping Engine (Phase 3)

Purpose:
    Encapsulates schema transformation logic from
    SOURCE_CUSTOMER_V1 → TARGET_ERP_CUSTOMER_V1.
"""

from transformation_rules import TransformationRules

# class MappingEngine:
#     """
#     Handles record-level transformations.
#     """

#     def transform_record(self, row: dict) -> dict:
#         """
#         Apply schema mapping rules to a single record.
#         """

#         street = row.get("StreetAddress", "")
#         house_no = row.get("HouseNo", "")

#         if house_no:
#             street = f"{street} {house_no}"

#         return {
#             "CustomerID": row.get("CustNo"),
#             "Name": row.get("CompanyName"),
#             "Street": street if street else None,
#             "City": row.get("Town"),
#             "PostalCode": row.get("ZipCode"),
#             "Country": row.get("CountryCode"),
#             "LastBusinessActivityDate": row.get("LastOrderDate"),
#             "Status": "active"
#         }

class MappingEngine:

    def transform_record(self, row: dict) -> dict:

        return {
            "CustomerID": row.get("CustNo"),
            "Name": row.get("CompanyName"),

            "Street": TransformationRules.build_street(
                row.get("StreetAddress"),
                row.get("HouseNo")
            ),

            "City": row.get("Town"),
            "PostalCode": row.get("ZipCode"),

            "Country": TransformationRules.normalize_country(
                row.get("CountryCode")
            ),

            "LastBusinessActivityDate": row.get("LastOrderDate"),

            "Status": TransformationRules.derive_status(
                row.get("LastOrderDate")
            )
        }