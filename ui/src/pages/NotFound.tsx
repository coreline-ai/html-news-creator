import { Link } from "react-router-dom";
import { FileQuestion } from "lucide-react";
import { Button } from "@/components/ui/button";
import { EmptyState } from "@/components/EmptyState";

export function NotFound() {
  return (
    <div className="mx-auto max-w-[1200px] px-6 py-6">
      <EmptyState
        icon={FileQuestion}
        title="Page not found"
        description="The route you requested does not exist."
        action={
          <Button asChild size="sm" variant="outline">
            <Link to="/">Go home</Link>
          </Button>
        }
      />
    </div>
  );
}

export default NotFound;
