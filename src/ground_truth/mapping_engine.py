"""
BenchmarkForge - Mapping Engine (Phase 3)

Purpose:
    Encapsulates schema transformation logic from
    SOURCE_CUSTOMER_V1 → TARGET_ERP_CUSTOMER_V1.
"""

from src.ground_truth.transformation_rules import TransformationRules
# from transformation_rules import TransformationRules        # Only for direct use via console

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