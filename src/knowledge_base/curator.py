class KnowledgeCurator:
    def __init__(self, knowledge_manager, compliance_checker):
        self.knowledge_manager = knowledge_manager
        self.compliance_checker = compliance_checker
    
    def curate_knowledge(self, new_data):
        """Refine and update the knowledge base with new information."""
        if self.compliance_checker.is_compliant(new_data):
            curated_data = self.knowledge_manager.transform_data(new_data)
            self.knowledge_manager.update_knowledge_base(curated_data)
            return curated_data
        else:
            raise ValueError("Data not compliant with regulations")
