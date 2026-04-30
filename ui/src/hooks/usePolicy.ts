import {
  useMutation,
  useQuery,
  useQueryClient,
  type UseMutationResult,
  type UseQueryResult,
} from "@tanstack/react-query";
import { apiFetch } from "@/lib/api";

/**
 * `editorial_policy.yaml` is a free-form mapping (the backend just merges a
 * runtime override on top of the on-disk yaml). We keep the type loose and
 * let consumers narrow per-section.
 */
export type Policy = Record<string, unknown>;

export interface PolicyResponse {
  policy: Policy;
}

export const POLICY_QUERY_KEY = ["policy"] as const;

/** GET /api/policy — yaml + runtime override merged. */
export function usePolicy(): UseQueryResult<Policy, Error> {
  return useQuery<Policy, Error>({
    queryKey: POLICY_QUERY_KEY,
    queryFn: async () => {
      const data = await apiFetch<PolicyResponse>("/api/policy");
      return data?.policy ?? {};
    },
  });
}

/**
 * PUT /api/policy — replaces the runtime override (volatile, not persisted
 * to disk). The body shape is `{ patch: <nested mapping> }`.
 */
export function useUpdatePolicy(): UseMutationResult<
  Policy,
  Error,
  { patch: Policy }
> {
  const qc = useQueryClient();
  return useMutation<Policy, Error, { patch: Policy }>({
    mutationFn: async ({ patch }) => {
      const data = await apiFetch<PolicyResponse>("/api/policy", {
        method: "PUT",
        body: JSON.stringify({ patch }),
      });
      return data?.policy ?? {};
    },
    onSuccess: (policy) => {
      qc.setQueryData(POLICY_QUERY_KEY, policy);
    },
  });
}
