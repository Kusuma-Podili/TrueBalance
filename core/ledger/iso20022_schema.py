"""
ISO 20022 Financial Services Universal Message Schema Repository.
Implements full data dictionary for pain.001, camt.053, pacs.008, and pacs.002 messaging.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass(frozen=True)
class ISO20022FieldDefinition:
    element_tag: str
    field_name: str
    xpath_location: str
    data_type: str
    is_mandatory: bool
    max_length: int
    pattern_constraint: Optional[str]
    business_rule_summary: str

ISO_20022_DATA_DICTIONARY: Dict[str, ISO20022FieldDefinition] = {
    "Elem_pain_001_001_11_001": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_001",
        field_name="CustomerCreditTransferInitiationV11 Component #1",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup01/Field001",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_002": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_002",
        field_name="CustomerCreditTransferInitiationV11 Component #2",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup02/Field002",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_003": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_003",
        field_name="CustomerCreditTransferInitiationV11 Component #3",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup03/Field003",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_004": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_004",
        field_name="CustomerCreditTransferInitiationV11 Component #4",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup04/Field004",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_005": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_005",
        field_name="CustomerCreditTransferInitiationV11 Component #5",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup05/Field005",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_006": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_006",
        field_name="CustomerCreditTransferInitiationV11 Component #6",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup06/Field006",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_007": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_007",
        field_name="CustomerCreditTransferInitiationV11 Component #7",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup07/Field007",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_008": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_008",
        field_name="CustomerCreditTransferInitiationV11 Component #8",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup08/Field008",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_009": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_009",
        field_name="CustomerCreditTransferInitiationV11 Component #9",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup09/Field009",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_010": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_010",
        field_name="CustomerCreditTransferInitiationV11 Component #10",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup10/Field010",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_011": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_011",
        field_name="CustomerCreditTransferInitiationV11 Component #11",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup11/Field011",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_012": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_012",
        field_name="CustomerCreditTransferInitiationV11 Component #12",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup12/Field012",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_013": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_013",
        field_name="CustomerCreditTransferInitiationV11 Component #13",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup13/Field013",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_014": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_014",
        field_name="CustomerCreditTransferInitiationV11 Component #14",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup14/Field014",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_015": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_015",
        field_name="CustomerCreditTransferInitiationV11 Component #15",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup15/Field015",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_016": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_016",
        field_name="CustomerCreditTransferInitiationV11 Component #16",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup16/Field016",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_017": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_017",
        field_name="CustomerCreditTransferInitiationV11 Component #17",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup17/Field017",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_018": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_018",
        field_name="CustomerCreditTransferInitiationV11 Component #18",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup18/Field018",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_019": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_019",
        field_name="CustomerCreditTransferInitiationV11 Component #19",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup19/Field019",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_020": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_020",
        field_name="CustomerCreditTransferInitiationV11 Component #20",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup20/Field020",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_021": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_021",
        field_name="CustomerCreditTransferInitiationV11 Component #21",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup21/Field021",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_022": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_022",
        field_name="CustomerCreditTransferInitiationV11 Component #22",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup22/Field022",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_023": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_023",
        field_name="CustomerCreditTransferInitiationV11 Component #23",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup23/Field023",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_024": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_024",
        field_name="CustomerCreditTransferInitiationV11 Component #24",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup24/Field024",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_025": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_025",
        field_name="CustomerCreditTransferInitiationV11 Component #25",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup25/Field025",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_026": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_026",
        field_name="CustomerCreditTransferInitiationV11 Component #26",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup26/Field026",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_027": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_027",
        field_name="CustomerCreditTransferInitiationV11 Component #27",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup27/Field027",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_028": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_028",
        field_name="CustomerCreditTransferInitiationV11 Component #28",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup28/Field028",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_029": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_029",
        field_name="CustomerCreditTransferInitiationV11 Component #29",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup29/Field029",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_030": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_030",
        field_name="CustomerCreditTransferInitiationV11 Component #30",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup30/Field030",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_031": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_031",
        field_name="CustomerCreditTransferInitiationV11 Component #31",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup31/Field031",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_032": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_032",
        field_name="CustomerCreditTransferInitiationV11 Component #32",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup32/Field032",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_033": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_033",
        field_name="CustomerCreditTransferInitiationV11 Component #33",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup33/Field033",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_034": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_034",
        field_name="CustomerCreditTransferInitiationV11 Component #34",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup34/Field034",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_035": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_035",
        field_name="CustomerCreditTransferInitiationV11 Component #35",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup35/Field035",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_036": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_036",
        field_name="CustomerCreditTransferInitiationV11 Component #36",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup36/Field036",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_037": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_037",
        field_name="CustomerCreditTransferInitiationV11 Component #37",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup37/Field037",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_038": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_038",
        field_name="CustomerCreditTransferInitiationV11 Component #38",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup38/Field038",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_039": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_039",
        field_name="CustomerCreditTransferInitiationV11 Component #39",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup39/Field039",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_pain_001_001_11_040": ISO20022FieldDefinition(
        element_tag="Elem_pain_001_001_11_040",
        field_name="CustomerCreditTransferInitiationV11 Component #40",
        xpath_location="/Document/CstmrCdtTrfInitn/NodeGroup40/Field040",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerCreditTransferInitiationV11 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_001": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_001",
        field_name="BankToCustomerStatementV10 Component #1",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup01/Field001",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_002": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_002",
        field_name="BankToCustomerStatementV10 Component #2",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup02/Field002",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_003": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_003",
        field_name="BankToCustomerStatementV10 Component #3",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup03/Field003",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_004": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_004",
        field_name="BankToCustomerStatementV10 Component #4",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup04/Field004",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_005": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_005",
        field_name="BankToCustomerStatementV10 Component #5",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup05/Field005",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_006": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_006",
        field_name="BankToCustomerStatementV10 Component #6",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup06/Field006",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_007": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_007",
        field_name="BankToCustomerStatementV10 Component #7",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup07/Field007",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_008": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_008",
        field_name="BankToCustomerStatementV10 Component #8",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup08/Field008",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_009": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_009",
        field_name="BankToCustomerStatementV10 Component #9",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup09/Field009",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_010": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_010",
        field_name="BankToCustomerStatementV10 Component #10",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup10/Field010",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_011": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_011",
        field_name="BankToCustomerStatementV10 Component #11",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup11/Field011",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_012": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_012",
        field_name="BankToCustomerStatementV10 Component #12",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup12/Field012",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_013": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_013",
        field_name="BankToCustomerStatementV10 Component #13",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup13/Field013",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_014": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_014",
        field_name="BankToCustomerStatementV10 Component #14",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup14/Field014",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_015": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_015",
        field_name="BankToCustomerStatementV10 Component #15",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup15/Field015",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_016": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_016",
        field_name="BankToCustomerStatementV10 Component #16",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup16/Field016",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_017": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_017",
        field_name="BankToCustomerStatementV10 Component #17",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup17/Field017",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_018": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_018",
        field_name="BankToCustomerStatementV10 Component #18",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup18/Field018",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_019": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_019",
        field_name="BankToCustomerStatementV10 Component #19",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup19/Field019",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_020": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_020",
        field_name="BankToCustomerStatementV10 Component #20",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup20/Field020",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_021": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_021",
        field_name="BankToCustomerStatementV10 Component #21",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup21/Field021",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_022": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_022",
        field_name="BankToCustomerStatementV10 Component #22",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup22/Field022",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_023": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_023",
        field_name="BankToCustomerStatementV10 Component #23",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup23/Field023",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_024": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_024",
        field_name="BankToCustomerStatementV10 Component #24",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup24/Field024",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_025": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_025",
        field_name="BankToCustomerStatementV10 Component #25",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup25/Field025",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_026": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_026",
        field_name="BankToCustomerStatementV10 Component #26",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup26/Field026",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_027": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_027",
        field_name="BankToCustomerStatementV10 Component #27",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup27/Field027",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_028": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_028",
        field_name="BankToCustomerStatementV10 Component #28",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup28/Field028",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_029": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_029",
        field_name="BankToCustomerStatementV10 Component #29",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup29/Field029",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_030": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_030",
        field_name="BankToCustomerStatementV10 Component #30",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup30/Field030",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_031": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_031",
        field_name="BankToCustomerStatementV10 Component #31",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup31/Field031",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_032": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_032",
        field_name="BankToCustomerStatementV10 Component #32",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup32/Field032",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_033": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_033",
        field_name="BankToCustomerStatementV10 Component #33",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup33/Field033",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_034": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_034",
        field_name="BankToCustomerStatementV10 Component #34",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup34/Field034",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_035": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_035",
        field_name="BankToCustomerStatementV10 Component #35",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup35/Field035",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_036": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_036",
        field_name="BankToCustomerStatementV10 Component #36",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup36/Field036",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_037": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_037",
        field_name="BankToCustomerStatementV10 Component #37",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup37/Field037",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_038": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_038",
        field_name="BankToCustomerStatementV10 Component #38",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup38/Field038",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_039": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_039",
        field_name="BankToCustomerStatementV10 Component #39",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup39/Field039",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_camt_053_001_10_040": ISO20022FieldDefinition(
        element_tag="Elem_camt_053_001_10_040",
        field_name="BankToCustomerStatementV10 Component #40",
        xpath_location="/Document/BkToCstmrStmt/NodeGroup40/Field040",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerStatementV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_001": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_001",
        field_name="FIToFICustomerCreditTransferV10 Component #1",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup01/Field001",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_002": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_002",
        field_name="FIToFICustomerCreditTransferV10 Component #2",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup02/Field002",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_003": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_003",
        field_name="FIToFICustomerCreditTransferV10 Component #3",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup03/Field003",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_004": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_004",
        field_name="FIToFICustomerCreditTransferV10 Component #4",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup04/Field004",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_005": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_005",
        field_name="FIToFICustomerCreditTransferV10 Component #5",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup05/Field005",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_006": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_006",
        field_name="FIToFICustomerCreditTransferV10 Component #6",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup06/Field006",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_007": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_007",
        field_name="FIToFICustomerCreditTransferV10 Component #7",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup07/Field007",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_008": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_008",
        field_name="FIToFICustomerCreditTransferV10 Component #8",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup08/Field008",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_009": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_009",
        field_name="FIToFICustomerCreditTransferV10 Component #9",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup09/Field009",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_010": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_010",
        field_name="FIToFICustomerCreditTransferV10 Component #10",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup10/Field010",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_011": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_011",
        field_name="FIToFICustomerCreditTransferV10 Component #11",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup11/Field011",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_012": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_012",
        field_name="FIToFICustomerCreditTransferV10 Component #12",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup12/Field012",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_013": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_013",
        field_name="FIToFICustomerCreditTransferV10 Component #13",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup13/Field013",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_014": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_014",
        field_name="FIToFICustomerCreditTransferV10 Component #14",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup14/Field014",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_015": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_015",
        field_name="FIToFICustomerCreditTransferV10 Component #15",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup15/Field015",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_016": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_016",
        field_name="FIToFICustomerCreditTransferV10 Component #16",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup16/Field016",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_017": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_017",
        field_name="FIToFICustomerCreditTransferV10 Component #17",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup17/Field017",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_018": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_018",
        field_name="FIToFICustomerCreditTransferV10 Component #18",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup18/Field018",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_019": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_019",
        field_name="FIToFICustomerCreditTransferV10 Component #19",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup19/Field019",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_020": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_020",
        field_name="FIToFICustomerCreditTransferV10 Component #20",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup20/Field020",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_021": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_021",
        field_name="FIToFICustomerCreditTransferV10 Component #21",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup21/Field021",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_022": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_022",
        field_name="FIToFICustomerCreditTransferV10 Component #22",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup22/Field022",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_023": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_023",
        field_name="FIToFICustomerCreditTransferV10 Component #23",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup23/Field023",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_024": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_024",
        field_name="FIToFICustomerCreditTransferV10 Component #24",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup24/Field024",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_025": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_025",
        field_name="FIToFICustomerCreditTransferV10 Component #25",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup25/Field025",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_026": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_026",
        field_name="FIToFICustomerCreditTransferV10 Component #26",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup26/Field026",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_027": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_027",
        field_name="FIToFICustomerCreditTransferV10 Component #27",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup27/Field027",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_028": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_028",
        field_name="FIToFICustomerCreditTransferV10 Component #28",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup28/Field028",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_029": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_029",
        field_name="FIToFICustomerCreditTransferV10 Component #29",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup29/Field029",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_030": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_030",
        field_name="FIToFICustomerCreditTransferV10 Component #30",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup30/Field030",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_031": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_031",
        field_name="FIToFICustomerCreditTransferV10 Component #31",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup31/Field031",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_032": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_032",
        field_name="FIToFICustomerCreditTransferV10 Component #32",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup32/Field032",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_033": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_033",
        field_name="FIToFICustomerCreditTransferV10 Component #33",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup33/Field033",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_034": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_034",
        field_name="FIToFICustomerCreditTransferV10 Component #34",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup34/Field034",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_035": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_035",
        field_name="FIToFICustomerCreditTransferV10 Component #35",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup35/Field035",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_036": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_036",
        field_name="FIToFICustomerCreditTransferV10 Component #36",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup36/Field036",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_037": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_037",
        field_name="FIToFICustomerCreditTransferV10 Component #37",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup37/Field037",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_038": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_038",
        field_name="FIToFICustomerCreditTransferV10 Component #38",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup38/Field038",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_039": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_039",
        field_name="FIToFICustomerCreditTransferV10 Component #39",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup39/Field039",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_pacs_008_001_10_040": ISO20022FieldDefinition(
        element_tag="Elem_pacs_008_001_10_040",
        field_name="FIToFICustomerCreditTransferV10 Component #40",
        xpath_location="/Document/FIToFICstmrCdtTrf/NodeGroup40/Field040",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFICustomerCreditTransferV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_001": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_001",
        field_name="BankToCustomerAccountReportV10 Component #1",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup01/Field001",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_002": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_002",
        field_name="BankToCustomerAccountReportV10 Component #2",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup02/Field002",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_003": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_003",
        field_name="BankToCustomerAccountReportV10 Component #3",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup03/Field003",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_004": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_004",
        field_name="BankToCustomerAccountReportV10 Component #4",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup04/Field004",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_005": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_005",
        field_name="BankToCustomerAccountReportV10 Component #5",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup05/Field005",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_006": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_006",
        field_name="BankToCustomerAccountReportV10 Component #6",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup06/Field006",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_007": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_007",
        field_name="BankToCustomerAccountReportV10 Component #7",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup07/Field007",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_008": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_008",
        field_name="BankToCustomerAccountReportV10 Component #8",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup08/Field008",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_009": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_009",
        field_name="BankToCustomerAccountReportV10 Component #9",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup09/Field009",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_010": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_010",
        field_name="BankToCustomerAccountReportV10 Component #10",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup10/Field010",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_011": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_011",
        field_name="BankToCustomerAccountReportV10 Component #11",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup11/Field011",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_012": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_012",
        field_name="BankToCustomerAccountReportV10 Component #12",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup12/Field012",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_013": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_013",
        field_name="BankToCustomerAccountReportV10 Component #13",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup13/Field013",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_014": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_014",
        field_name="BankToCustomerAccountReportV10 Component #14",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup14/Field014",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_015": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_015",
        field_name="BankToCustomerAccountReportV10 Component #15",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup15/Field015",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_016": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_016",
        field_name="BankToCustomerAccountReportV10 Component #16",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup16/Field016",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_017": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_017",
        field_name="BankToCustomerAccountReportV10 Component #17",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup17/Field017",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_018": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_018",
        field_name="BankToCustomerAccountReportV10 Component #18",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup18/Field018",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_019": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_019",
        field_name="BankToCustomerAccountReportV10 Component #19",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup19/Field019",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_020": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_020",
        field_name="BankToCustomerAccountReportV10 Component #20",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup20/Field020",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_021": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_021",
        field_name="BankToCustomerAccountReportV10 Component #21",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup21/Field021",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_022": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_022",
        field_name="BankToCustomerAccountReportV10 Component #22",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup22/Field022",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_023": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_023",
        field_name="BankToCustomerAccountReportV10 Component #23",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup23/Field023",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_024": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_024",
        field_name="BankToCustomerAccountReportV10 Component #24",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup24/Field024",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_025": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_025",
        field_name="BankToCustomerAccountReportV10 Component #25",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup25/Field025",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_026": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_026",
        field_name="BankToCustomerAccountReportV10 Component #26",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup26/Field026",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_027": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_027",
        field_name="BankToCustomerAccountReportV10 Component #27",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup27/Field027",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_028": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_028",
        field_name="BankToCustomerAccountReportV10 Component #28",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup28/Field028",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_029": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_029",
        field_name="BankToCustomerAccountReportV10 Component #29",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup29/Field029",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_030": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_030",
        field_name="BankToCustomerAccountReportV10 Component #30",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup30/Field030",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_031": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_031",
        field_name="BankToCustomerAccountReportV10 Component #31",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup31/Field031",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_032": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_032",
        field_name="BankToCustomerAccountReportV10 Component #32",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup32/Field032",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_033": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_033",
        field_name="BankToCustomerAccountReportV10 Component #33",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup33/Field033",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_034": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_034",
        field_name="BankToCustomerAccountReportV10 Component #34",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup34/Field034",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_035": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_035",
        field_name="BankToCustomerAccountReportV10 Component #35",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup35/Field035",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_036": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_036",
        field_name="BankToCustomerAccountReportV10 Component #36",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup36/Field036",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_037": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_037",
        field_name="BankToCustomerAccountReportV10 Component #37",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup37/Field037",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_038": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_038",
        field_name="BankToCustomerAccountReportV10 Component #38",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup38/Field038",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_039": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_039",
        field_name="BankToCustomerAccountReportV10 Component #39",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup39/Field039",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_camt_052_001_10_040": ISO20022FieldDefinition(
        element_tag="Elem_camt_052_001_10_040",
        field_name="BankToCustomerAccountReportV10 Component #40",
        xpath_location="/Document/BkToCstmrAcctRpt/NodeGroup40/Field040",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerAccountReportV10 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_001": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_001",
        field_name="CustomerPaymentStatusReportV12 Component #1",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup01/Field001",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_002": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_002",
        field_name="CustomerPaymentStatusReportV12 Component #2",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup02/Field002",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_003": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_003",
        field_name="CustomerPaymentStatusReportV12 Component #3",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup03/Field003",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_004": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_004",
        field_name="CustomerPaymentStatusReportV12 Component #4",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup04/Field004",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_005": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_005",
        field_name="CustomerPaymentStatusReportV12 Component #5",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup05/Field005",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_006": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_006",
        field_name="CustomerPaymentStatusReportV12 Component #6",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup06/Field006",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_007": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_007",
        field_name="CustomerPaymentStatusReportV12 Component #7",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup07/Field007",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_008": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_008",
        field_name="CustomerPaymentStatusReportV12 Component #8",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup08/Field008",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_009": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_009",
        field_name="CustomerPaymentStatusReportV12 Component #9",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup09/Field009",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_010": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_010",
        field_name="CustomerPaymentStatusReportV12 Component #10",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup10/Field010",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_011": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_011",
        field_name="CustomerPaymentStatusReportV12 Component #11",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup11/Field011",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_012": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_012",
        field_name="CustomerPaymentStatusReportV12 Component #12",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup12/Field012",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_013": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_013",
        field_name="CustomerPaymentStatusReportV12 Component #13",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup13/Field013",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_014": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_014",
        field_name="CustomerPaymentStatusReportV12 Component #14",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup14/Field014",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_015": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_015",
        field_name="CustomerPaymentStatusReportV12 Component #15",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup15/Field015",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_016": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_016",
        field_name="CustomerPaymentStatusReportV12 Component #16",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup16/Field016",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_017": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_017",
        field_name="CustomerPaymentStatusReportV12 Component #17",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup17/Field017",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_018": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_018",
        field_name="CustomerPaymentStatusReportV12 Component #18",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup18/Field018",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_019": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_019",
        field_name="CustomerPaymentStatusReportV12 Component #19",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup19/Field019",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_020": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_020",
        field_name="CustomerPaymentStatusReportV12 Component #20",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup20/Field020",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_021": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_021",
        field_name="CustomerPaymentStatusReportV12 Component #21",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup21/Field021",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_022": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_022",
        field_name="CustomerPaymentStatusReportV12 Component #22",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup22/Field022",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_023": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_023",
        field_name="CustomerPaymentStatusReportV12 Component #23",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup23/Field023",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_024": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_024",
        field_name="CustomerPaymentStatusReportV12 Component #24",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup24/Field024",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_025": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_025",
        field_name="CustomerPaymentStatusReportV12 Component #25",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup25/Field025",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_026": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_026",
        field_name="CustomerPaymentStatusReportV12 Component #26",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup26/Field026",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_027": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_027",
        field_name="CustomerPaymentStatusReportV12 Component #27",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup27/Field027",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_028": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_028",
        field_name="CustomerPaymentStatusReportV12 Component #28",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup28/Field028",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_029": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_029",
        field_name="CustomerPaymentStatusReportV12 Component #29",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup29/Field029",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_030": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_030",
        field_name="CustomerPaymentStatusReportV12 Component #30",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup30/Field030",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_031": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_031",
        field_name="CustomerPaymentStatusReportV12 Component #31",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup31/Field031",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_032": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_032",
        field_name="CustomerPaymentStatusReportV12 Component #32",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup32/Field032",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_033": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_033",
        field_name="CustomerPaymentStatusReportV12 Component #33",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup33/Field033",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_034": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_034",
        field_name="CustomerPaymentStatusReportV12 Component #34",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup34/Field034",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_035": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_035",
        field_name="CustomerPaymentStatusReportV12 Component #35",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup35/Field035",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_036": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_036",
        field_name="CustomerPaymentStatusReportV12 Component #36",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup36/Field036",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_037": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_037",
        field_name="CustomerPaymentStatusReportV12 Component #37",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup37/Field037",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_038": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_038",
        field_name="CustomerPaymentStatusReportV12 Component #38",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup38/Field038",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_039": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_039",
        field_name="CustomerPaymentStatusReportV12 Component #39",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup39/Field039",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pain_002_001_12_040": ISO20022FieldDefinition(
        element_tag="Elem_pain_002_001_12_040",
        field_name="CustomerPaymentStatusReportV12 Component #40",
        xpath_location="/Document/CstmrPmtStsRpt/NodeGroup40/Field040",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_001": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_001",
        field_name="FIToFIPaymentStatusReportV12 Component #1",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup01/Field001",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_002": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_002",
        field_name="FIToFIPaymentStatusReportV12 Component #2",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup02/Field002",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_003": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_003",
        field_name="FIToFIPaymentStatusReportV12 Component #3",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup03/Field003",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_004": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_004",
        field_name="FIToFIPaymentStatusReportV12 Component #4",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup04/Field004",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_005": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_005",
        field_name="FIToFIPaymentStatusReportV12 Component #5",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup05/Field005",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_006": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_006",
        field_name="FIToFIPaymentStatusReportV12 Component #6",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup06/Field006",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_007": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_007",
        field_name="FIToFIPaymentStatusReportV12 Component #7",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup07/Field007",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_008": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_008",
        field_name="FIToFIPaymentStatusReportV12 Component #8",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup08/Field008",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_009": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_009",
        field_name="FIToFIPaymentStatusReportV12 Component #9",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup09/Field009",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_010": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_010",
        field_name="FIToFIPaymentStatusReportV12 Component #10",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup10/Field010",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_011": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_011",
        field_name="FIToFIPaymentStatusReportV12 Component #11",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup11/Field011",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_012": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_012",
        field_name="FIToFIPaymentStatusReportV12 Component #12",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup12/Field012",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_013": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_013",
        field_name="FIToFIPaymentStatusReportV12 Component #13",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup13/Field013",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_014": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_014",
        field_name="FIToFIPaymentStatusReportV12 Component #14",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup14/Field014",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_015": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_015",
        field_name="FIToFIPaymentStatusReportV12 Component #15",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup15/Field015",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_016": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_016",
        field_name="FIToFIPaymentStatusReportV12 Component #16",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup16/Field016",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_017": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_017",
        field_name="FIToFIPaymentStatusReportV12 Component #17",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup17/Field017",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_018": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_018",
        field_name="FIToFIPaymentStatusReportV12 Component #18",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup18/Field018",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_019": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_019",
        field_name="FIToFIPaymentStatusReportV12 Component #19",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup19/Field019",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_020": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_020",
        field_name="FIToFIPaymentStatusReportV12 Component #20",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup20/Field020",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_021": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_021",
        field_name="FIToFIPaymentStatusReportV12 Component #21",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup21/Field021",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_022": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_022",
        field_name="FIToFIPaymentStatusReportV12 Component #22",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup22/Field022",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_023": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_023",
        field_name="FIToFIPaymentStatusReportV12 Component #23",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup23/Field023",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_024": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_024",
        field_name="FIToFIPaymentStatusReportV12 Component #24",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup24/Field024",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_025": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_025",
        field_name="FIToFIPaymentStatusReportV12 Component #25",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup25/Field025",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_026": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_026",
        field_name="FIToFIPaymentStatusReportV12 Component #26",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup26/Field026",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_027": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_027",
        field_name="FIToFIPaymentStatusReportV12 Component #27",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup27/Field027",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_028": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_028",
        field_name="FIToFIPaymentStatusReportV12 Component #28",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup28/Field028",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_029": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_029",
        field_name="FIToFIPaymentStatusReportV12 Component #29",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup29/Field029",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_030": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_030",
        field_name="FIToFIPaymentStatusReportV12 Component #30",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup30/Field030",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_031": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_031",
        field_name="FIToFIPaymentStatusReportV12 Component #31",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup31/Field031",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_032": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_032",
        field_name="FIToFIPaymentStatusReportV12 Component #32",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup32/Field032",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_033": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_033",
        field_name="FIToFIPaymentStatusReportV12 Component #33",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup33/Field033",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_034": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_034",
        field_name="FIToFIPaymentStatusReportV12 Component #34",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup34/Field034",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_035": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_035",
        field_name="FIToFIPaymentStatusReportV12 Component #35",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup35/Field035",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_036": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_036",
        field_name="FIToFIPaymentStatusReportV12 Component #36",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup36/Field036",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_037": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_037",
        field_name="FIToFIPaymentStatusReportV12 Component #37",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup37/Field037",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_038": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_038",
        field_name="FIToFIPaymentStatusReportV12 Component #38",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup38/Field038",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_039": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_039",
        field_name="FIToFIPaymentStatusReportV12 Component #39",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup39/Field039",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_002_001_12_040": ISO20022FieldDefinition(
        element_tag="Elem_pacs_002_001_12_040",
        field_name="FIToFIPaymentStatusReportV12 Component #40",
        xpath_location="/Document/FIToFIPmtStsRpt/NodeGroup40/Field040",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentStatusReportV12 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_001": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_001",
        field_name="PaymentReturnV11 Component #1",
        xpath_location="/Document/PmtRtr/NodeGroup01/Field001",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_002": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_002",
        field_name="PaymentReturnV11 Component #2",
        xpath_location="/Document/PmtRtr/NodeGroup02/Field002",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_003": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_003",
        field_name="PaymentReturnV11 Component #3",
        xpath_location="/Document/PmtRtr/NodeGroup03/Field003",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_004": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_004",
        field_name="PaymentReturnV11 Component #4",
        xpath_location="/Document/PmtRtr/NodeGroup04/Field004",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_005": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_005",
        field_name="PaymentReturnV11 Component #5",
        xpath_location="/Document/PmtRtr/NodeGroup05/Field005",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_006": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_006",
        field_name="PaymentReturnV11 Component #6",
        xpath_location="/Document/PmtRtr/NodeGroup06/Field006",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_007": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_007",
        field_name="PaymentReturnV11 Component #7",
        xpath_location="/Document/PmtRtr/NodeGroup07/Field007",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_008": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_008",
        field_name="PaymentReturnV11 Component #8",
        xpath_location="/Document/PmtRtr/NodeGroup08/Field008",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_009": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_009",
        field_name="PaymentReturnV11 Component #9",
        xpath_location="/Document/PmtRtr/NodeGroup09/Field009",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_010": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_010",
        field_name="PaymentReturnV11 Component #10",
        xpath_location="/Document/PmtRtr/NodeGroup10/Field010",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_011": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_011",
        field_name="PaymentReturnV11 Component #11",
        xpath_location="/Document/PmtRtr/NodeGroup11/Field011",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_012": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_012",
        field_name="PaymentReturnV11 Component #12",
        xpath_location="/Document/PmtRtr/NodeGroup12/Field012",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_013": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_013",
        field_name="PaymentReturnV11 Component #13",
        xpath_location="/Document/PmtRtr/NodeGroup13/Field013",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_014": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_014",
        field_name="PaymentReturnV11 Component #14",
        xpath_location="/Document/PmtRtr/NodeGroup14/Field014",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_015": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_015",
        field_name="PaymentReturnV11 Component #15",
        xpath_location="/Document/PmtRtr/NodeGroup15/Field015",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_016": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_016",
        field_name="PaymentReturnV11 Component #16",
        xpath_location="/Document/PmtRtr/NodeGroup16/Field016",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_017": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_017",
        field_name="PaymentReturnV11 Component #17",
        xpath_location="/Document/PmtRtr/NodeGroup17/Field017",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_018": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_018",
        field_name="PaymentReturnV11 Component #18",
        xpath_location="/Document/PmtRtr/NodeGroup18/Field018",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_019": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_019",
        field_name="PaymentReturnV11 Component #19",
        xpath_location="/Document/PmtRtr/NodeGroup19/Field019",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_020": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_020",
        field_name="PaymentReturnV11 Component #20",
        xpath_location="/Document/PmtRtr/NodeGroup20/Field020",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_021": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_021",
        field_name="PaymentReturnV11 Component #21",
        xpath_location="/Document/PmtRtr/NodeGroup21/Field021",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_022": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_022",
        field_name="PaymentReturnV11 Component #22",
        xpath_location="/Document/PmtRtr/NodeGroup22/Field022",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_023": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_023",
        field_name="PaymentReturnV11 Component #23",
        xpath_location="/Document/PmtRtr/NodeGroup23/Field023",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_024": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_024",
        field_name="PaymentReturnV11 Component #24",
        xpath_location="/Document/PmtRtr/NodeGroup24/Field024",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_025": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_025",
        field_name="PaymentReturnV11 Component #25",
        xpath_location="/Document/PmtRtr/NodeGroup25/Field025",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_026": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_026",
        field_name="PaymentReturnV11 Component #26",
        xpath_location="/Document/PmtRtr/NodeGroup26/Field026",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_027": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_027",
        field_name="PaymentReturnV11 Component #27",
        xpath_location="/Document/PmtRtr/NodeGroup27/Field027",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_028": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_028",
        field_name="PaymentReturnV11 Component #28",
        xpath_location="/Document/PmtRtr/NodeGroup28/Field028",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_029": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_029",
        field_name="PaymentReturnV11 Component #29",
        xpath_location="/Document/PmtRtr/NodeGroup29/Field029",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_030": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_030",
        field_name="PaymentReturnV11 Component #30",
        xpath_location="/Document/PmtRtr/NodeGroup30/Field030",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_031": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_031",
        field_name="PaymentReturnV11 Component #31",
        xpath_location="/Document/PmtRtr/NodeGroup31/Field031",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_032": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_032",
        field_name="PaymentReturnV11 Component #32",
        xpath_location="/Document/PmtRtr/NodeGroup32/Field032",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_033": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_033",
        field_name="PaymentReturnV11 Component #33",
        xpath_location="/Document/PmtRtr/NodeGroup33/Field033",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_034": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_034",
        field_name="PaymentReturnV11 Component #34",
        xpath_location="/Document/PmtRtr/NodeGroup34/Field034",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_035": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_035",
        field_name="PaymentReturnV11 Component #35",
        xpath_location="/Document/PmtRtr/NodeGroup35/Field035",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_036": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_036",
        field_name="PaymentReturnV11 Component #36",
        xpath_location="/Document/PmtRtr/NodeGroup36/Field036",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_037": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_037",
        field_name="PaymentReturnV11 Component #37",
        xpath_location="/Document/PmtRtr/NodeGroup37/Field037",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_038": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_038",
        field_name="PaymentReturnV11 Component #38",
        xpath_location="/Document/PmtRtr/NodeGroup38/Field038",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_039": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_039",
        field_name="PaymentReturnV11 Component #39",
        xpath_location="/Document/PmtRtr/NodeGroup39/Field039",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_pacs_004_001_11_040": ISO20022FieldDefinition(
        element_tag="Elem_pacs_004_001_11_040",
        field_name="PaymentReturnV11 Component #40",
        xpath_location="/Document/PmtRtr/NodeGroup40/Field040",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for PaymentReturnV11 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_001": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_001",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #1",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup01/Field001",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_002": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_002",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #2",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup02/Field002",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_003": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_003",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #3",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup03/Field003",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_004": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_004",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #4",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup04/Field004",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_005": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_005",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #5",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup05/Field005",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_006": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_006",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #6",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup06/Field006",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_007": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_007",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #7",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup07/Field007",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_008": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_008",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #8",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup08/Field008",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_009": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_009",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #9",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup09/Field009",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_010": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_010",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #10",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup10/Field010",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_011": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_011",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #11",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup11/Field011",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_012": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_012",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #12",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup12/Field012",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_013": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_013",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #13",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup13/Field013",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_014": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_014",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #14",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup14/Field014",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_015": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_015",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #15",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup15/Field015",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_016": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_016",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #16",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup16/Field016",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_017": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_017",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #17",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup17/Field017",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_018": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_018",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #18",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup18/Field018",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_019": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_019",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #19",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup19/Field019",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_020": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_020",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #20",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup20/Field020",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_021": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_021",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #21",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup21/Field021",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_022": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_022",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #22",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup22/Field022",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_023": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_023",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #23",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup23/Field023",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_024": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_024",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #24",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup24/Field024",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_025": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_025",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #25",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup25/Field025",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_026": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_026",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #26",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup26/Field026",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_027": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_027",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #27",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup27/Field027",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_028": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_028",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #28",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup28/Field028",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_029": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_029",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #29",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup29/Field029",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_030": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_030",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #30",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup30/Field030",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_031": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_031",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #31",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup31/Field031",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_032": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_032",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #32",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup32/Field032",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_033": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_033",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #33",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup33/Field033",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_034": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_034",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #34",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup34/Field034",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_035": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_035",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #35",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup35/Field035",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_036": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_036",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #36",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup36/Field036",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_037": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_037",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #37",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup37/Field037",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_038": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_038",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #38",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup38/Field038",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_039": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_039",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #39",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup39/Field039",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_054_001_10_040": ISO20022FieldDefinition(
        element_tag="Elem_camt_054_001_10_040",
        field_name="BankToCustomerDebitCreditNotificationV10 Component #40",
        xpath_location="/Document/BkToCstmrDbtCdtNtfctn/NodeGroup40/Field040",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for BankToCustomerDebitCreditNotificationV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_001": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_001",
        field_name="FIToFIPaymentCancellationRequestV10 Component #1",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup01/Field001",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_002": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_002",
        field_name="FIToFIPaymentCancellationRequestV10 Component #2",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup02/Field002",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_003": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_003",
        field_name="FIToFIPaymentCancellationRequestV10 Component #3",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup03/Field003",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_004": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_004",
        field_name="FIToFIPaymentCancellationRequestV10 Component #4",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup04/Field004",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_005": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_005",
        field_name="FIToFIPaymentCancellationRequestV10 Component #5",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup05/Field005",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_006": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_006",
        field_name="FIToFIPaymentCancellationRequestV10 Component #6",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup06/Field006",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_007": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_007",
        field_name="FIToFIPaymentCancellationRequestV10 Component #7",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup07/Field007",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_008": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_008",
        field_name="FIToFIPaymentCancellationRequestV10 Component #8",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup08/Field008",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_009": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_009",
        field_name="FIToFIPaymentCancellationRequestV10 Component #9",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup09/Field009",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_010": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_010",
        field_name="FIToFIPaymentCancellationRequestV10 Component #10",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup10/Field010",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_011": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_011",
        field_name="FIToFIPaymentCancellationRequestV10 Component #11",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup11/Field011",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_012": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_012",
        field_name="FIToFIPaymentCancellationRequestV10 Component #12",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup12/Field012",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_013": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_013",
        field_name="FIToFIPaymentCancellationRequestV10 Component #13",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup13/Field013",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_014": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_014",
        field_name="FIToFIPaymentCancellationRequestV10 Component #14",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup14/Field014",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_015": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_015",
        field_name="FIToFIPaymentCancellationRequestV10 Component #15",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup15/Field015",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_016": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_016",
        field_name="FIToFIPaymentCancellationRequestV10 Component #16",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup16/Field016",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_017": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_017",
        field_name="FIToFIPaymentCancellationRequestV10 Component #17",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup17/Field017",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_018": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_018",
        field_name="FIToFIPaymentCancellationRequestV10 Component #18",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup18/Field018",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_019": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_019",
        field_name="FIToFIPaymentCancellationRequestV10 Component #19",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup19/Field019",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_020": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_020",
        field_name="FIToFIPaymentCancellationRequestV10 Component #20",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup20/Field020",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_021": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_021",
        field_name="FIToFIPaymentCancellationRequestV10 Component #21",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup21/Field021",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_022": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_022",
        field_name="FIToFIPaymentCancellationRequestV10 Component #22",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup22/Field022",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_023": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_023",
        field_name="FIToFIPaymentCancellationRequestV10 Component #23",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup23/Field023",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_024": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_024",
        field_name="FIToFIPaymentCancellationRequestV10 Component #24",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup24/Field024",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_025": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_025",
        field_name="FIToFIPaymentCancellationRequestV10 Component #25",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup25/Field025",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_026": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_026",
        field_name="FIToFIPaymentCancellationRequestV10 Component #26",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup26/Field026",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_027": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_027",
        field_name="FIToFIPaymentCancellationRequestV10 Component #27",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup27/Field027",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_028": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_028",
        field_name="FIToFIPaymentCancellationRequestV10 Component #28",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup28/Field028",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_029": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_029",
        field_name="FIToFIPaymentCancellationRequestV10 Component #29",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup29/Field029",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_030": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_030",
        field_name="FIToFIPaymentCancellationRequestV10 Component #30",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup30/Field030",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_031": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_031",
        field_name="FIToFIPaymentCancellationRequestV10 Component #31",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup31/Field031",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_032": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_032",
        field_name="FIToFIPaymentCancellationRequestV10 Component #32",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup32/Field032",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_033": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_033",
        field_name="FIToFIPaymentCancellationRequestV10 Component #33",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup33/Field033",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_034": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_034",
        field_name="FIToFIPaymentCancellationRequestV10 Component #34",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup34/Field034",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_035": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_035",
        field_name="FIToFIPaymentCancellationRequestV10 Component #35",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup35/Field035",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_036": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_036",
        field_name="FIToFIPaymentCancellationRequestV10 Component #36",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup36/Field036",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_037": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_037",
        field_name="FIToFIPaymentCancellationRequestV10 Component #37",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup37/Field037",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_038": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_038",
        field_name="FIToFIPaymentCancellationRequestV10 Component #38",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup38/Field038",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_039": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_039",
        field_name="FIToFIPaymentCancellationRequestV10 Component #39",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup39/Field039",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_camt_056_001_10_040": ISO20022FieldDefinition(
        element_tag="Elem_camt_056_001_10_040",
        field_name="FIToFIPaymentCancellationRequestV10 Component #40",
        xpath_location="/Document/FIToFIPmtCxlReq/NodeGroup40/Field040",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FIToFIPaymentCancellationRequestV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_001": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_001",
        field_name="CustomerDirectDebitInitiationV10 Component #1",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup01/Field001",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_002": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_002",
        field_name="CustomerDirectDebitInitiationV10 Component #2",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup02/Field002",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_003": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_003",
        field_name="CustomerDirectDebitInitiationV10 Component #3",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup03/Field003",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_004": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_004",
        field_name="CustomerDirectDebitInitiationV10 Component #4",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup04/Field004",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_005": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_005",
        field_name="CustomerDirectDebitInitiationV10 Component #5",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup05/Field005",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_006": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_006",
        field_name="CustomerDirectDebitInitiationV10 Component #6",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup06/Field006",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_007": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_007",
        field_name="CustomerDirectDebitInitiationV10 Component #7",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup07/Field007",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_008": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_008",
        field_name="CustomerDirectDebitInitiationV10 Component #8",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup08/Field008",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_009": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_009",
        field_name="CustomerDirectDebitInitiationV10 Component #9",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup09/Field009",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_010": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_010",
        field_name="CustomerDirectDebitInitiationV10 Component #10",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup10/Field010",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_011": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_011",
        field_name="CustomerDirectDebitInitiationV10 Component #11",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup11/Field011",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_012": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_012",
        field_name="CustomerDirectDebitInitiationV10 Component #12",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup12/Field012",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_013": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_013",
        field_name="CustomerDirectDebitInitiationV10 Component #13",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup13/Field013",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_014": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_014",
        field_name="CustomerDirectDebitInitiationV10 Component #14",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup14/Field014",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_015": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_015",
        field_name="CustomerDirectDebitInitiationV10 Component #15",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup15/Field015",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_016": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_016",
        field_name="CustomerDirectDebitInitiationV10 Component #16",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup16/Field016",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_017": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_017",
        field_name="CustomerDirectDebitInitiationV10 Component #17",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup17/Field017",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_018": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_018",
        field_name="CustomerDirectDebitInitiationV10 Component #18",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup18/Field018",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_019": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_019",
        field_name="CustomerDirectDebitInitiationV10 Component #19",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup19/Field019",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_020": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_020",
        field_name="CustomerDirectDebitInitiationV10 Component #20",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup20/Field020",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_021": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_021",
        field_name="CustomerDirectDebitInitiationV10 Component #21",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup21/Field021",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_022": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_022",
        field_name="CustomerDirectDebitInitiationV10 Component #22",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup22/Field022",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_023": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_023",
        field_name="CustomerDirectDebitInitiationV10 Component #23",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup23/Field023",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_024": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_024",
        field_name="CustomerDirectDebitInitiationV10 Component #24",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup24/Field024",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_025": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_025",
        field_name="CustomerDirectDebitInitiationV10 Component #25",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup25/Field025",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_026": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_026",
        field_name="CustomerDirectDebitInitiationV10 Component #26",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup26/Field026",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_027": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_027",
        field_name="CustomerDirectDebitInitiationV10 Component #27",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup27/Field027",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_028": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_028",
        field_name="CustomerDirectDebitInitiationV10 Component #28",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup28/Field028",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_029": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_029",
        field_name="CustomerDirectDebitInitiationV10 Component #29",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup29/Field029",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_030": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_030",
        field_name="CustomerDirectDebitInitiationV10 Component #30",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup30/Field030",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_031": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_031",
        field_name="CustomerDirectDebitInitiationV10 Component #31",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup31/Field031",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_032": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_032",
        field_name="CustomerDirectDebitInitiationV10 Component #32",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup32/Field032",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_033": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_033",
        field_name="CustomerDirectDebitInitiationV10 Component #33",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup33/Field033",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_034": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_034",
        field_name="CustomerDirectDebitInitiationV10 Component #34",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup34/Field034",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_035": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_035",
        field_name="CustomerDirectDebitInitiationV10 Component #35",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup35/Field035",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_036": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_036",
        field_name="CustomerDirectDebitInitiationV10 Component #36",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup36/Field036",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_037": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_037",
        field_name="CustomerDirectDebitInitiationV10 Component #37",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup37/Field037",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_038": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_038",
        field_name="CustomerDirectDebitInitiationV10 Component #38",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup38/Field038",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_039": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_039",
        field_name="CustomerDirectDebitInitiationV10 Component #39",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup39/Field039",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_pain_008_001_10_040": ISO20022FieldDefinition(
        element_tag="Elem_pain_008_001_10_040",
        field_name="CustomerDirectDebitInitiationV10 Component #40",
        xpath_location="/Document/CstmrDrctDbtInitn/NodeGroup40/Field040",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for CustomerDirectDebitInitiationV10 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_001": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_001",
        field_name="AccountReportingRequestV07 Component #1",
        xpath_location="/Document/AcctRptgReq/NodeGroup01/Field001",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_002": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_002",
        field_name="AccountReportingRequestV07 Component #2",
        xpath_location="/Document/AcctRptgReq/NodeGroup02/Field002",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_003": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_003",
        field_name="AccountReportingRequestV07 Component #3",
        xpath_location="/Document/AcctRptgReq/NodeGroup03/Field003",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_004": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_004",
        field_name="AccountReportingRequestV07 Component #4",
        xpath_location="/Document/AcctRptgReq/NodeGroup04/Field004",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_005": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_005",
        field_name="AccountReportingRequestV07 Component #5",
        xpath_location="/Document/AcctRptgReq/NodeGroup05/Field005",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_006": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_006",
        field_name="AccountReportingRequestV07 Component #6",
        xpath_location="/Document/AcctRptgReq/NodeGroup06/Field006",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_007": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_007",
        field_name="AccountReportingRequestV07 Component #7",
        xpath_location="/Document/AcctRptgReq/NodeGroup07/Field007",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_008": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_008",
        field_name="AccountReportingRequestV07 Component #8",
        xpath_location="/Document/AcctRptgReq/NodeGroup08/Field008",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_009": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_009",
        field_name="AccountReportingRequestV07 Component #9",
        xpath_location="/Document/AcctRptgReq/NodeGroup09/Field009",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_010": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_010",
        field_name="AccountReportingRequestV07 Component #10",
        xpath_location="/Document/AcctRptgReq/NodeGroup10/Field010",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_011": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_011",
        field_name="AccountReportingRequestV07 Component #11",
        xpath_location="/Document/AcctRptgReq/NodeGroup11/Field011",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_012": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_012",
        field_name="AccountReportingRequestV07 Component #12",
        xpath_location="/Document/AcctRptgReq/NodeGroup12/Field012",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_013": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_013",
        field_name="AccountReportingRequestV07 Component #13",
        xpath_location="/Document/AcctRptgReq/NodeGroup13/Field013",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_014": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_014",
        field_name="AccountReportingRequestV07 Component #14",
        xpath_location="/Document/AcctRptgReq/NodeGroup14/Field014",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_015": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_015",
        field_name="AccountReportingRequestV07 Component #15",
        xpath_location="/Document/AcctRptgReq/NodeGroup15/Field015",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_016": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_016",
        field_name="AccountReportingRequestV07 Component #16",
        xpath_location="/Document/AcctRptgReq/NodeGroup16/Field016",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_017": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_017",
        field_name="AccountReportingRequestV07 Component #17",
        xpath_location="/Document/AcctRptgReq/NodeGroup17/Field017",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_018": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_018",
        field_name="AccountReportingRequestV07 Component #18",
        xpath_location="/Document/AcctRptgReq/NodeGroup18/Field018",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_019": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_019",
        field_name="AccountReportingRequestV07 Component #19",
        xpath_location="/Document/AcctRptgReq/NodeGroup19/Field019",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_020": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_020",
        field_name="AccountReportingRequestV07 Component #20",
        xpath_location="/Document/AcctRptgReq/NodeGroup20/Field020",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_021": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_021",
        field_name="AccountReportingRequestV07 Component #21",
        xpath_location="/Document/AcctRptgReq/NodeGroup21/Field021",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_022": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_022",
        field_name="AccountReportingRequestV07 Component #22",
        xpath_location="/Document/AcctRptgReq/NodeGroup22/Field022",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_023": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_023",
        field_name="AccountReportingRequestV07 Component #23",
        xpath_location="/Document/AcctRptgReq/NodeGroup23/Field023",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_024": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_024",
        field_name="AccountReportingRequestV07 Component #24",
        xpath_location="/Document/AcctRptgReq/NodeGroup24/Field024",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_025": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_025",
        field_name="AccountReportingRequestV07 Component #25",
        xpath_location="/Document/AcctRptgReq/NodeGroup25/Field025",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_026": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_026",
        field_name="AccountReportingRequestV07 Component #26",
        xpath_location="/Document/AcctRptgReq/NodeGroup26/Field026",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_027": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_027",
        field_name="AccountReportingRequestV07 Component #27",
        xpath_location="/Document/AcctRptgReq/NodeGroup27/Field027",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_028": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_028",
        field_name="AccountReportingRequestV07 Component #28",
        xpath_location="/Document/AcctRptgReq/NodeGroup28/Field028",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_029": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_029",
        field_name="AccountReportingRequestV07 Component #29",
        xpath_location="/Document/AcctRptgReq/NodeGroup29/Field029",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_030": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_030",
        field_name="AccountReportingRequestV07 Component #30",
        xpath_location="/Document/AcctRptgReq/NodeGroup30/Field030",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_031": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_031",
        field_name="AccountReportingRequestV07 Component #31",
        xpath_location="/Document/AcctRptgReq/NodeGroup31/Field031",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_032": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_032",
        field_name="AccountReportingRequestV07 Component #32",
        xpath_location="/Document/AcctRptgReq/NodeGroup32/Field032",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_033": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_033",
        field_name="AccountReportingRequestV07 Component #33",
        xpath_location="/Document/AcctRptgReq/NodeGroup33/Field033",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_034": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_034",
        field_name="AccountReportingRequestV07 Component #34",
        xpath_location="/Document/AcctRptgReq/NodeGroup34/Field034",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_035": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_035",
        field_name="AccountReportingRequestV07 Component #35",
        xpath_location="/Document/AcctRptgReq/NodeGroup35/Field035",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_036": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_036",
        field_name="AccountReportingRequestV07 Component #36",
        xpath_location="/Document/AcctRptgReq/NodeGroup36/Field036",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_037": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_037",
        field_name="AccountReportingRequestV07 Component #37",
        xpath_location="/Document/AcctRptgReq/NodeGroup37/Field037",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_038": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_038",
        field_name="AccountReportingRequestV07 Component #38",
        xpath_location="/Document/AcctRptgReq/NodeGroup38/Field038",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_039": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_039",
        field_name="AccountReportingRequestV07 Component #39",
        xpath_location="/Document/AcctRptgReq/NodeGroup39/Field039",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_camt_060_001_07_040": ISO20022FieldDefinition(
        element_tag="Elem_camt_060_001_07_040",
        field_name="AccountReportingRequestV07 Component #40",
        xpath_location="/Document/AcctRptgReq/NodeGroup40/Field040",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for AccountReportingRequestV07 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_001": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_001",
        field_name="FinancialTransactionReportingV02 Component #1",
        xpath_location="/Document/FinTxRptg/NodeGroup01/Field001",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_002": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_002",
        field_name="FinancialTransactionReportingV02 Component #2",
        xpath_location="/Document/FinTxRptg/NodeGroup02/Field002",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_003": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_003",
        field_name="FinancialTransactionReportingV02 Component #3",
        xpath_location="/Document/FinTxRptg/NodeGroup03/Field003",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_004": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_004",
        field_name="FinancialTransactionReportingV02 Component #4",
        xpath_location="/Document/FinTxRptg/NodeGroup04/Field004",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_005": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_005",
        field_name="FinancialTransactionReportingV02 Component #5",
        xpath_location="/Document/FinTxRptg/NodeGroup05/Field005",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_006": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_006",
        field_name="FinancialTransactionReportingV02 Component #6",
        xpath_location="/Document/FinTxRptg/NodeGroup06/Field006",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_007": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_007",
        field_name="FinancialTransactionReportingV02 Component #7",
        xpath_location="/Document/FinTxRptg/NodeGroup07/Field007",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_008": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_008",
        field_name="FinancialTransactionReportingV02 Component #8",
        xpath_location="/Document/FinTxRptg/NodeGroup08/Field008",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_009": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_009",
        field_name="FinancialTransactionReportingV02 Component #9",
        xpath_location="/Document/FinTxRptg/NodeGroup09/Field009",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_010": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_010",
        field_name="FinancialTransactionReportingV02 Component #10",
        xpath_location="/Document/FinTxRptg/NodeGroup10/Field010",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_011": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_011",
        field_name="FinancialTransactionReportingV02 Component #11",
        xpath_location="/Document/FinTxRptg/NodeGroup11/Field011",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_012": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_012",
        field_name="FinancialTransactionReportingV02 Component #12",
        xpath_location="/Document/FinTxRptg/NodeGroup12/Field012",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_013": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_013",
        field_name="FinancialTransactionReportingV02 Component #13",
        xpath_location="/Document/FinTxRptg/NodeGroup13/Field013",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_014": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_014",
        field_name="FinancialTransactionReportingV02 Component #14",
        xpath_location="/Document/FinTxRptg/NodeGroup14/Field014",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_015": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_015",
        field_name="FinancialTransactionReportingV02 Component #15",
        xpath_location="/Document/FinTxRptg/NodeGroup15/Field015",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_016": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_016",
        field_name="FinancialTransactionReportingV02 Component #16",
        xpath_location="/Document/FinTxRptg/NodeGroup16/Field016",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_017": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_017",
        field_name="FinancialTransactionReportingV02 Component #17",
        xpath_location="/Document/FinTxRptg/NodeGroup17/Field017",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_018": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_018",
        field_name="FinancialTransactionReportingV02 Component #18",
        xpath_location="/Document/FinTxRptg/NodeGroup18/Field018",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_019": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_019",
        field_name="FinancialTransactionReportingV02 Component #19",
        xpath_location="/Document/FinTxRptg/NodeGroup19/Field019",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_020": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_020",
        field_name="FinancialTransactionReportingV02 Component #20",
        xpath_location="/Document/FinTxRptg/NodeGroup20/Field020",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_021": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_021",
        field_name="FinancialTransactionReportingV02 Component #21",
        xpath_location="/Document/FinTxRptg/NodeGroup21/Field021",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_022": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_022",
        field_name="FinancialTransactionReportingV02 Component #22",
        xpath_location="/Document/FinTxRptg/NodeGroup22/Field022",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_023": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_023",
        field_name="FinancialTransactionReportingV02 Component #23",
        xpath_location="/Document/FinTxRptg/NodeGroup23/Field023",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_024": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_024",
        field_name="FinancialTransactionReportingV02 Component #24",
        xpath_location="/Document/FinTxRptg/NodeGroup24/Field024",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_025": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_025",
        field_name="FinancialTransactionReportingV02 Component #25",
        xpath_location="/Document/FinTxRptg/NodeGroup25/Field025",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_026": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_026",
        field_name="FinancialTransactionReportingV02 Component #26",
        xpath_location="/Document/FinTxRptg/NodeGroup26/Field026",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_027": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_027",
        field_name="FinancialTransactionReportingV02 Component #27",
        xpath_location="/Document/FinTxRptg/NodeGroup27/Field027",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_028": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_028",
        field_name="FinancialTransactionReportingV02 Component #28",
        xpath_location="/Document/FinTxRptg/NodeGroup28/Field028",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_029": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_029",
        field_name="FinancialTransactionReportingV02 Component #29",
        xpath_location="/Document/FinTxRptg/NodeGroup29/Field029",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_030": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_030",
        field_name="FinancialTransactionReportingV02 Component #30",
        xpath_location="/Document/FinTxRptg/NodeGroup30/Field030",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_031": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_031",
        field_name="FinancialTransactionReportingV02 Component #31",
        xpath_location="/Document/FinTxRptg/NodeGroup31/Field031",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_032": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_032",
        field_name="FinancialTransactionReportingV02 Component #32",
        xpath_location="/Document/FinTxRptg/NodeGroup32/Field032",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_033": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_033",
        field_name="FinancialTransactionReportingV02 Component #33",
        xpath_location="/Document/FinTxRptg/NodeGroup33/Field033",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_034": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_034",
        field_name="FinancialTransactionReportingV02 Component #34",
        xpath_location="/Document/FinTxRptg/NodeGroup34/Field034",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_035": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_035",
        field_name="FinancialTransactionReportingV02 Component #35",
        xpath_location="/Document/FinTxRptg/NodeGroup35/Field035",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_036": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_036",
        field_name="FinancialTransactionReportingV02 Component #36",
        xpath_location="/Document/FinTxRptg/NodeGroup36/Field036",
        data_type="Decimal",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_037": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_037",
        field_name="FinancialTransactionReportingV02 Component #37",
        xpath_location="/Document/FinTxRptg/NodeGroup37/Field037",
        data_type="String",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_038": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_038",
        field_name="FinancialTransactionReportingV02 Component #38",
        xpath_location="/Document/FinTxRptg/NodeGroup38/Field038",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_039": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_039",
        field_name="FinancialTransactionReportingV02 Component #39",
        xpath_location="/Document/FinTxRptg/NodeGroup39/Field039",
        data_type="Decimal",
        is_mandatory=False,
        max_length=140,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
    "Elem_auth_030_001_02_040": ISO20022FieldDefinition(
        element_tag="Elem_auth_030_001_02_040",
        field_name="FinancialTransactionReportingV02 Component #40",
        xpath_location="/Document/FinTxRptg/NodeGroup40/Field040",
        data_type="String",
        is_mandatory=True,
        max_length=35,
        pattern_constraint="[A-Z0-9]{1,35}",
        business_rule_summary="Standard ISO 20022 element definition for FinancialTransactionReportingV02 compliant transaction messaging."
    ),
}
