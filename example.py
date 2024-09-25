from knowledge_base.curator import KnowledgeCurator
from knowledge_base.knowledge_manager import KnowledgeManager
from knowledge_base.compliance_checker import ComplianceChecker

compliance_rules = ["GDPR", "HIPAA"]  # Example compliance rules
compliance_checker = ComplianceChecker(compliance_rules)
knowledge_manager = KnowledgeManager()

curator = KnowledgeCurator(knowledge_manager, compliance_checker)
new_data = {...}  # Example new data

curated_data = curator.curate_knowledge(new_data)
