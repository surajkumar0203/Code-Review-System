from rest_framework import serializers

class Start_taskSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)
    pr_number = serializers.IntegerField()
    github_token = serializers.CharField(
        required=False, 
        write_only=True, 
        allow_blank=True,
    )

    def validate_github_token(self, value):
        """
        Custom validation for GitHub token if provided.
        """
        if value:  # Validate only if a token is provided
            if len(value) != 40:  # GitHub tokens are typically 40 characters long
                raise serializers.ValidationError("Invalid GitHub token length.")
            
        return value
